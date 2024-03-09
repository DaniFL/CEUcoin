from blockchain.Blockchain import *
from user.Wallet import *
from gui.App import App
from databaseManager.BlockchainManager import BlockchainManager

def main():
    app = App() 
    app.run()    


if __name__ == "__main__":
    # main()
    blockchain_manager = BlockchainManager()
    blockchain = blockchain_manager.get_blockchain()
    
    for block in blockchain.get_chain():
        print(block)
    # wallet1 = Wallet(100, "12")
    # wallet2 = Wallet(0, "11")  # Crear otra instancia de user.Wallet para el destinatario

    # t = wallet1.send(10, wallet2)  # Usar la instancia wallet2 como destinatario
    # blockchain.add_block(t)
    # print("\n", blockchain.chain[-1], "\n")

    # t1 = wallet1.send(11, wallet2)  # Usar la instancia wallet2 como destinatario
    # blockchain.add_block(t1)
    # print(blockchain.chain[-1], "\n")

    # t2 = wallet1.send(10, wallet2)  # Usar la instancia wallet2 como destinatario
    # blockchain.add_block(t2)
    # print(blockchain.chain[-1], "\n")



