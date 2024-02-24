import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Blockchain blockchain = new Blockchain();
        Wallet wallet = new Wallet(100, "12");
        Transaction t = wallet.send(10, "11");
        blockchain.addBlock(t);
        System.out.println(blockchain);
        Transaction t1 = wallet.send(11, "11");
        blockchain.addBlock(t1);
        System.out.println(blockchain);
        Transaction t2 = wallet.send(10, "11");
        blockchain.addBlock(t2);
        System.out.println(blockchain);
    }


   /* private static void initializeBlockchain() {
        // Crear el bloque génesis
        Block genesisBlock = new Block("0", new Transaction("genesis_sender", "genesis_recipient", 0));
        // Agregar el bloque génesis al blockchain
        blockchain.addBlock(genesisBlock);
    }
*/
    // añadimos bloques llamando a add dentro de bc


}
