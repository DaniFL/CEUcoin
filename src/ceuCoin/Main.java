package ceuCoin;
import user.*;

public class Main {

    public static void main(String[] args) {
        Blockchain blockchain = new Blockchain();
        Wallet wallet1 = new Wallet(100, "12");
        Wallet wallet2 = new Wallet(0, "11"); // Crear otra instancia de user.Wallet para el destinatario
        Transaction t = wallet1.send(10, wallet2); // Usar la instancia wallet2 como destinatario
        blockchain.addBlock(t);
        System.out.println(blockchain);

        Transaction t1 = wallet1.send(11, wallet2); // Usar la instancia wallet2 como destinatario
        blockchain.addBlock(t1);
        System.out.println(blockchain);

        Transaction t2 = wallet1.send(10, wallet2); // Usar la instancia wallet2 como destinatario
        blockchain.addBlock(t2);
        System.out.println(blockchain);
    }



   /* private static void initializeBlockchain() {
        // Crear el bloque génesis
        ceuCoin.Block genesisBlock = new ceuCoin.Block("0", new ceuCoin.Transaction("genesis_sender", "genesis_recipient", 0));
        // Agregar el bloque génesis al blockchain
        blockchain.addBlock(genesisBlock);
    }
*/
    // añadimos bloques llamando a add dentro de bc


}
