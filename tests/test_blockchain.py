import unittest
from blockchain.Blockchain import Blockchain
from blockchain.Block import Block
from blockchain.Transaction import Transaction
from user.Wallet import Wallet

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        # Configuración común para todas las pruebas
        self.blockchain = Blockchain()
        self.wallet1 = Wallet(100, "12")
        self.wallet2 = Wallet(0, "11")

    def test_add_block(self):
        # Verifica que se añade un bloque correctamente
        t = self.wallet1.send(10, self.wallet2)
        self.blockchain.add_block(t)
        self.assertEqual(len(self.blockchain.get_chain()), 2)

    def test_get_latest_block(self):
        # Verifica que se obtiene el último bloque correctamente
        t = self.wallet1.send(10, self.wallet2)
        self.blockchain.add_block(t)
        latest_block = self.blockchain.get_latest_block()
        self.assertIsInstance(latest_block, Block)

    def test_genesis_block(self):
        # Verifica que el bloque génesis se crea correctamente
        self.assertEqual(len(self.blockchain.get_chain()), 1)
        genesis_block = self.blockchain.get_latest_block()
        self.assertIsInstance(genesis_block, Block)
        self.assertEqual(genesis_block.get_height(), 0)

    # Agrega más pruebas según sea necesario

if __name__ == '__main__':
    unittest.main()
