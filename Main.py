from blockchain.Blockchain import *
from user.Wallet import *
from gui.App import App
from gui.Login import Login
from databaseManager.BlockchainManager import BlockchainManager

def main(blockchainmanager):
    login = Login(blockchainmanager) 
    login.run()   


if __name__ == "__main__":
    blockchainmanager = BlockchainManager()
    # blockchain = blockchainmanager.get_blockchain()
    main(blockchainmanager)



