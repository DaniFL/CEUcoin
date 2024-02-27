import org.junit.Test;

import static org.junit.Assert.*;

public class MainTest {

    @Test
    public void testWalletInitialization() {
        Wallet wallet = new Wallet(50.0, "wallet123");
        assertEquals("Initial balance is not as expected", 50.0, wallet.getBalance(), 0.001);
        assertEquals("ID is not as expected", "wallet123", wallet.getCardId());
    }

    @Test
    public void testSimpleTransaction() {
        Wallet senderWallet = new Wallet(100.0, "sender123");
        Wallet recipientWallet = new Wallet(50.0, "recipient456");

        Transaction transaction = senderWallet.send(30.0, "recipient456");

        assertNotNull("Transaction should not be null", transaction);
        assertEquals("Sender balance is not as expected after sending funds", 70.0, senderWallet.getBalance(), 0.001);
    }
    @Test
    public void testBlockInitialization() {
        Transaction transaction = new Transaction("sender", "recipient", 10.0);
        Block block = new Block("previousHash", transaction);

        assertNotNull("Block hash should not be null", block.getHash());
    }

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

