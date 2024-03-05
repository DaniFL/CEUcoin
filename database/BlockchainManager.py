import sqlite3
from CEUCoin.Block import Block
from CEUCoin.Blockchain import Blockchain
from CEUCoin.Transaction import Transaction
from datetime import datetime

class BlockchainManager:
    DATABASE_URL = "CEUCoinDB.db"

    def __init__(self):
        try:
            self.connection = sqlite3.connect(self.DATABASE_URL)
            self.connection.execute("PRAGMA foreign_keys=ON")
            print("Database connection opened.")

            self.create_tables()
        except sqlite3.Error as e:
            print("Error connecting to SQLite:", e)

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS Transaction (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    block_height INTEGER REFERENCES Block(height),
                    sender TEXT,
                    recipient TEXT,
                    amount REAL,
                    datetime TEXT
                )
            """
            cursor.execute(query)

            query = """
                CREATE TABLE IF NOT EXISTS Block (
                    height INTEGER PRIMARY KEY,
                    previous_hash TEXT UNIQUE,
                    hash TEXT UNIQUE,
                    datetime TEXT,
                    difficulty INTEGER,
                    nonce INTEGER
                )
            """
            cursor.execute(query)

            self.connection.commit()
        except sqlite3.Error as e:
            print("Error creating tables:", e)

    def add_block(self, block):
        try:
            cursor = self.connection.cursor()

            query = """
                INSERT INTO Block (height, previous_hash, hash, datetime, difficulty, nonce)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (block.get_height(), block.get_previous_hash(), block.get_hash(),
                                   block.get_datetime().isoformat(), block.get_difficulty(), block.get_nonce()))

            transaction = block.get_transaction()

            query = """
                INSERT INTO Transaction (block_height, sender, recipient, amount, datetime)
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

            query = "SELECT * FROM Block"
            cursor.execute(query)
            blocks = cursor.fetchall()

            for block_data in blocks:
                height, previous_hash, hash_value, datetime_str, difficulty, nonce = block_data
                block = Block(height, previous_hash, hash_value, datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f'), difficulty, nonce)

                query = "SELECT * FROM Transaction WHERE block_height = ?"
                cursor.execute(query, (height,))
                transactions = cursor.fetchall()

                for transaction_data in transactions:
                    _, sender, recipient, amount, transaction_datetime_str = transaction_data
                    transaction = Transaction(sender, recipient, amount, datetime.strptime(transaction_datetime_str, '%Y-%m-%dT%H:%M:%S.%f'))
                    block.add_transaction(transaction)

                blockchain.add_block(block)

            return blockchain
        except sqlite3.Error as e:
            print("Error retrieving blockchain:", e)
            return None
