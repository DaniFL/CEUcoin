import sqlite3
from blockchain.Block import *
from blockchain.Blockchain import *
from blockchain.Transaction import *
from user.User import *
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
                    datetime TEXT
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
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """
            cursor.execute(query)

            query = "INSERT INTO Userdata (username, password) VALUES (?, ?)"
            cursor.execute(query, ("user", "user"))

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
                    INSERT INTO Transactions (block_height, sender, recipient, amount, datetime)
                    VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(query, (0, "System", "System", 0, datetime.now().isoformat()))

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
                INSERT INTO Transactions (block_height, sender, recipient, amount, datetime)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (block.get_height(), transaction.get_sender(), transaction.get_recipient(),
                                   transaction.get_amount(), transaction.get_datetime().isoformat()))

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
                    _, _, sender, recipient, amount, transaction_datetime_str = transaction_data
                    transaction = Transaction(sender, recipient, amount, datetime.strptime(transaction_datetime_str, '%Y-%m-%dT%H:%M:%S.%f'))
                    

                block = Block(previous_hash, hash_value, transaction, datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f'), difficulty, nonce, height)

                blockchain.get_chain().append(block)

            return blockchain
        except sqlite3.Error as e:
            print("Error retrieving blockchain:", e)
            return None
        
    def check_user(self, username, password):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Userdata WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            userdata = cursor.fetchone()
            _, username, password = userdata
            return User(username, password)

        except sqlite3.Error as e:
            print("Error verifying user:", e)
            return None
        
    # def check_user(self, username, password):
    #     try:
    #         cursor = self.connection.cursor()
    #         query = "SELECT * FROM Userdata WHERE username = ? AND password = ?"
    #         cursor.execute(query, (username, password))
    #         userdata = cursor.fetchone()
            
    #         if userdata is not None:
    #             _, db_username, db_password = userdata
    #             return User(db_username, db_password)
    #         else:
    #             return None

    #     except sqlite3.Error as e:
    #         print("Error verifying user:", e)
    #         return None

