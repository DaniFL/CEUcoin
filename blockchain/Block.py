import hashlib
from datetime import datetime

class Block:
    # MINE_RATE = 4000

    def __init__(self, previous_hash, hash, transaction, datetime, difficulty, nonce, height):
        self.previous_hash = previous_hash
        self.hash = hash
        self.transaction = transaction
        self.datetime = datetime
        self.difficulty = difficulty
        self.nonce = nonce
        self.height = height

    # @classmethod
    # def genesis(cls, transaction):
    #     return cls("undefined", "genesis hash", transaction, datetime.now(), 5, 0, 0)

    @staticmethod
    def calculate_hash(previous_hash, transaction, datetime, difficulty, nonce, height):
        data_to_hash = previous_hash + str(transaction) + str(datetime) + str(difficulty) + str(nonce) + str(height)
        hash_bytes = hashlib.sha256(data_to_hash.encode()).digest()
        return hashlib.sha256(hash_bytes).hexdigest()

    @staticmethod
    def mine(previous_block, transaction):
        previous_hash = previous_block.hash
        difficulty = previous_block.difficulty
        hash_value = ""
        datetime_now = datetime.now()
        nonce = 0
        height = previous_block.height + 1

        while True:
            nonce += 1
            datetime_now = datetime.now()
            hash_value = Block.calculate_hash(previous_hash, transaction, datetime_now, difficulty, nonce, height)
            if hash_value.startswith("0" * difficulty):
                break

        return Block(previous_hash, hash_value, transaction, datetime_now, difficulty, nonce, height)

    def __str__(self):
        return f"\nBlock previous_hash='{self.previous_hash}', \nhash='{self.hash}', \ntransaction={self.transaction}, \ndatetime={self.datetime}, \ndifficulty={self.difficulty}, \nnonce={self.nonce})"

    def get_previous_hash(self):
        return self.previous_hash

    def get_hash(self):
        return self.hash

    def get_transaction(self):
        return self.transaction

    def get_datetime(self):
        return self.datetime

    def get_difficulty(self):
        return self.difficulty

    def get_nonce(self):
        return self.nonce

    def get_height(self):
        return self.height
