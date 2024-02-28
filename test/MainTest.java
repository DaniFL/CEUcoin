import ceuCoin.Block;
import ceuCoin.Transaction;
import org.junit.Test;
import user.Wallet;

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

        Transaction transaction = senderWallet.send(30.0, recipientWallet);

        assertNotNull("ceuCoin.Transaction should not be null", transaction);
        assertEquals("Sender balance is not as expected after sending funds", 70.0, senderWallet.getBalance(), 0.001);
    }

    /*
    @Test
    public void testBlockInitialization() {
        ceuCoin.Transaction transaction = new ceuCoin.Transaction("sender", "recipient", 10.0);
        ceuCoin.Block block = new ceuCoin.Block("previousHash", transaction);

        assertNotNull("ceuCoin.Block hash should not be null", block.getHash());
    }
     */

   @Test
   public void testSendMoney() {
       Wallet sender = new Wallet(100.0, "senderCardId");
       Wallet recipient = new Wallet(50.0, "recipientCardId");

       double amountToSend = 30.0;
       Transaction transaction = sender.send(amountToSend, recipient);

       assertNotNull(transaction);
       assertEquals(sender.getCardId(), transaction.sender);
       assertEquals(recipient.getCardId(), transaction.recipient);
       assertEquals(amountToSend, transaction.amount, 0.001);

       assertEquals(70.0, sender.getBalance(), 0.001);
       assertEquals(80.0, recipient.getBalance(), 0.001);
   }

    @Test
    public void testReceiveMoney() {
        Wallet recipient = new Wallet(50.0, "recipientCardId");

        double amountToReceive = 20.0;
        recipient.receive(amountToReceive);

        assertEquals(70.0, recipient.getBalance(), 0.001);
    }

    @Test
    public void testGetBalance() {
        Wallet wallet = new Wallet(100.0, "cardId");

        assertEquals(100.0, wallet.getBalance(), 0.001);
    }

    @Test
    public void testMineBlock() {
        Transaction transaction = new Transaction("sender123", "recipient456", 30.0);
        Block previousBlock = Block.genesis(transaction);

        Block minedBlock = Block.mine(previousBlock, transaction);

        assertNotNull(minedBlock);
        assertEquals(previousBlock.getHash(), minedBlock.getPreviousHash());
        assertNotNull(minedBlock.getHash());
        assertNotNull(minedBlock.getTransaction());
    }
}

