from ceu import Blockchain
from user.Wallet import Wallet

if __name__ == "__main__":
    blockchain = Blockchain()
    wallet1 = Wallet(100, "12")
    wallet2 = Wallet(0, "11")  # Crear otra instancia de user.Wallet para el destinatario

    t = wallet1.send(10, wallet2)  # Usar la instancia wallet2 como destinatario
    blockchain.add_block(t)
    print(blockchain)

    t1 = wallet1.send(11, wallet2)  # Usar la instancia wallet2 como destinatario
    blockchain.add_block(t1)
    print(blockchain)

    t2 = wallet1.send(10, wallet2)  # Usar la instancia wallet2 como destinatario
    blockchain.add_block(t2)
    print(blockchain)
