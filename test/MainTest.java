import org.junit.Test;
import static org.junit.Assert.*;

public class MainTest {

    @Test
    public void testInitialBalance() {
        Main wallet = new Main(100.0);
        assertEquals(100.0, wallet.getBalance(), 0.001);
    }

    @Test
    public void testDeposit() {
        Main wallet = new Main(50.0);
        wallet.deposit(30.0);
        assertEquals(80.0, wallet.getBalance(), 0.001);
    }

    @Test
    public void testWithdrawSufficientFunds() {
        Main wallet = new Main(50.0);
        wallet.withdraw(20.0);
        assertEquals(30.0, wallet.getBalance(), 0.001);
    }

    @Test
    public void testWithdrawInsufficientFunds() {
        Main wallet = new Main(30.0);
        wallet.withdraw(50.0);
        assertEquals(30.0, wallet.getBalance(), 0.001);
    }

    //Test para las clases que no son la Main
    @Test
    public void testCreateTransaction() {
        Wallet senderWallet = new Wallet();
        Wallet recipientWallet = new Wallet();
        Transaction transaction = senderWallet.createTransaction(recipientWallet.getPublicKey(), 50.0);

        assertTrue(transaction.isValid());
    }

    @Test
    public void testAddBlockToBlockchain() {
        Blockchain blockchain = new Blockchain();
        Block block = new Block(blockchain.getLatestBlock().calculateHash());
        blockchain.addBlock(block);

        assertTrue(blockchain.isValid());
    }

}
