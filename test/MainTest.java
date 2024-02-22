import org.junit.Test;

import java.util.Date;

import static org.junit.Assert.*;

public class MainTest {

    @Test
    public void testInitialBalance() {
        Wallet wallet = new Wallet(100.0);
        assertEquals(100.0, wallet.getBalance(), 0.001);
    }

    @Test
    public void testDeposit() {
        Wallet wallet = new Wallet(50.0);
        wallet.deposit(30.0);
        assertEquals(80.0, wallet.getBalance(), 0.001);
    }

    @Test
    public void testWithdrawSufficientFunds() {
        Wallet wallet = new Wallet(50.0);
        wallet.withdraw(20.0);
        assertEquals(30.0, wallet.getBalance(), 0.001);
    }

    @Test
    public void testWithdrawInsufficientFunds() {
        Wallet wallet = new Wallet(30.0);
        wallet.withdraw(50.0);
        assertEquals(30.0, wallet.getBalance(), 0.001);
    }


   // @Test
   /* public void testAddBlockToBlockchain() {
        Blockchain blockchain = new Blockchain();
        Block block = new Block(blockchain.getLatestBlock().calculateHash());
        blockchain.addBlock(block);

        assertTrue(blockchain.isValid());
    }
    */
   @Test
   public void testCalculateHash() {
       // Crear un bloque de prueba
       Block block1 = new Block("0", new Transaction("hash_sender_Alice", "hash_recipient_Bob", 10));
       Block block2 = new Block(block1.calculateHash(), new Transaction("hash_sender_Bob", "hash_recipient_Charlie", 5));

       // Calcular los hashes
       String hash1 = block1.calculateHash();
       String hash2 = block2.calculateHash();

       // Asegurar que los hashes no son nulos
       assertNotNull(hash1);
       assertNotNull(hash2);

       // Asegurar que los hashes son diferentes para bloques diferentes
       assertNotEquals(hash1, hash2);

       // Asegurar que el hash se calcula correctamente
       assertEquals(hash1, block1.calculateHash());
   }
}

