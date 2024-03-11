import sqlite3
import hashlib
from blockchain.Block import *
from blockchain.Blockchain import *
from blockchain.Transaction import *
from user.User import *
from user.Wallet import *
from datetime import datetime

class BlockchainManager:
    DATABASE_URL = "database/CEUCoinDB.db"

    def __init__(self):
        try:
            self.connection = sqlite3.connect(self.DATABASE_URL)
            self.connection.execute("PRAGMA foreign_keys=ON")
            print("Database connection opened.")

            self.create_tables()
            self.insert_genesis_block()
        except sqlite3.Error as e:
            print("Error connecting to SQLite:", e)

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS Transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    block_height INTEGER REFERENCES Blocks(height),
                    sender TEXT,
                    recipient TEXT,
                    amount REAL,
                    datetime TEXT,
                    state TEXT
                )
            """
            cursor.execute(query)

            query = """
                CREATE TABLE IF NOT EXISTS Blocks (
                    height INTEGER PRIMARY KEY,
                    previous_hash TEXT UNIQUE,
                    hash TEXT UNIQUE,
                    datetime TEXT,
                    difficulty INTEGER,
                    nonce INTEGER
                )
            """
            cursor.execute(query)

            query = """
                CREATE TABLE IF NOT EXISTS Userdata (
                    id TEXT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """
            cursor.execute(query)

            query = """
                CREATE TABLE IF NOT EXISTS Wallet (
                    card_id BLOB PRIMARY KEY,
                    user_id TEXT REFERENCES Userdata(id),
                    balance REAL
                )
            """
            cursor.execute(query)           

            self.connection.commit()
        except sqlite3.Error as e:
            print("Error creating tables:", e)

    def insert_genesis_block(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT COUNT(*) FROM Blocks"
            cursor.execute(query)
            count = cursor.fetchone()[0]

            if count == 0:
                query = """
                    INSERT INTO Blocks (height, previous_hash, hash, datetime, difficulty, nonce)
                    VALUES (?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (0, "undefined", "genesis hash", datetime.now().isoformat(), 5, 0))

                query = """
                    INSERT INTO Transactions (block_height, sender, recipient, amount, datetime, state)
                    VALUES (?, ?, ?, ?, ?, ?)
                """
                cursor.execute(query, (0, "System", "System", 0, datetime.now().isoformat(), "COMPLETED"))

                self.connection.commit()

        except sqlite3.Error as e:
            print("Error initializing blockchain:", e)  

    def add_block(self, block):
        try:
            cursor = self.connection.cursor()

            query = """
                INSERT INTO Blocks (height, previous_hash, hash, datetime, difficulty, nonce)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (block.get_height(), block.get_previous_hash(), block.get_hash(),
                                   block.get_datetime().isoformat(), block.get_difficulty(), block.get_nonce()))

            transaction = block.get_transaction()

            query = """
                INSERT INTO Transactions (block_height, sender, recipient, amount, datetime, state)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (block.get_height(), transaction.get_sender(), transaction.get_recipient(),
                                   transaction.get_amount(), transaction.get_datetime().isoformat(), transaction.get_state()))

            self.connection.commit()
        except sqlite3.Error as e:
            print("Error adding block:", e)

    def get_blockchain(self):
        try:
            blockchain = Blockchain()
            cursor = self.connection.cursor()

            query = "SELECT * FROM Blocks"
            cursor.execute(query)
            blocks = cursor.fetchall()

            for block_data in blocks:
                height, previous_hash, hash_value, datetime_str, difficulty, nonce = block_data
                
                query = "SELECT * FROM Transactions WHERE block_height = ?"
                cursor.execute(query, (height,))
                transactions = cursor.fetchall()

                for transaction_data in transactions:
                    _, _, sender, recipient, amount, transaction_datetime_str, state = transaction_data
                    transaction = Transaction.Transaction(sender, recipient, amount, datetime.strptime(transaction_datetime_str, '%Y-%m-%dT%H:%M:%S.%f'), state)
                    

                block = Block(previous_hash, hash_value, transaction, datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f'), difficulty, nonce, height)

                blockchain.get_chain().append(block)

            return blockchain
        except sqlite3.Error as e:
            print("Error retrieving blockchain:", e)
            return None
        
    def check_user(self, username, password):
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            cursor = self.connection.cursor()
            query = "SELECT * FROM Userdata WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password_hash))
            userdata = cursor.fetchone()
            
            if userdata is not None:
                id, username, password = userdata

                query = "SELECT * FROM Wallet WHERE user_id = ?"
                cursor.execute(query, (id,))
                wallet_data = cursor.fetchone()
                card_id, _, balance = wallet_data

                wallet = Wallet(balance, card_id)

                return User(id, username, password, wallet)
            else:
                return None

        except sqlite3.Error as e:
            print("Error verifying user:", e)
            return None
        
    def add_user(self, user):
        try:
            cursor = self.connection.cursor()

            query = "INSERT INTO Userdata (id, username, password) VALUES (?, ?, ?)"
            password_hash = hashlib.sha256(user.get_password().encode()).hexdigest()
            cursor.execute(query, (user.get_id(), user.get_username(), password_hash))

            query = "INSERT INTO Wallet (card_id, user_id, balance) VALUES (?, ?, ?)"
            cursor.execute(query, (user.get_wallet().get_card_id(), user.get_id(), user.get_wallet().get_balance())) 

            self.connection.commit()
        except sqlite3.Error as e:
            print("Error adding user:", e)
            return None
        
    def get_pending_transactions_of_user(self, user):
        try:
            cursor = self.connection.cursor()

            query = "SELECT * FROM Transactions WHERE recipient = ? AND state = ?"
            cursor.execute(query, (user.get_username(), "PENDING"))
            
            transactions = cursor.fetchall()
            pending_transactions = []

            for transaction_data in transactions:
                _, _, sender, recipient, amount, transaction_datetime_str, state = transaction_data
                transaction = Transaction(sender, recipient, amount, datetime.strptime(transaction_datetime_str, '%Y-%m-%dT%H:%M:%S.%f'), state)
                pending_transactions.append(transaction)
                    
            return pending_transactions
        except sqlite3.Error as e:
            print("Error retrieving transactions:", e)
            return None
        
    def update_transactions_of_user(self, user):
        try:
            cursor = self.connection.cursor()

            query = "UPDATE Transaction SET state = ? WHERE recipient = ? AND state = ?"
            cursor.execute(query, ("PENDING", user.get_username(), "PENDING"))
                    
        except sqlite3.Error as e:
            print("Error updating transactions:", e)
            return None



        

