from blockchain.Block import *
from blockchain.Transaction import *

class Blockchain:
    def __init__(self):
        self.chain = []
        # print(self.chain)

    def add_block(self, transaction):
        new_block = Block.mine(self.get_latest_block(), transaction)
        self.chain.append(new_block)

    def get_latest_block(self):
        return self.chain[-1]

    def get_chain(self):
        return self.chain

    def __str__(self):
        return f"Blockchain = {self.chain}"


