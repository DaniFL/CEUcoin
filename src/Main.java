import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static Blockchain blockchain;

    public static void main(String[] args) {
        System.out.println(LocalDate.now());
        blockchain = new Blockchain();
        // Inicializar el blockchain con un bloque génesis
        initializeBlockchain();
    }


    private static void initializeBlockchain() {
        // Crear el bloque génesis
        Block genesisBlock = new Block("0", new Transaction("genesis_sender", "genesis_recipient", 0));
        // Agregar el bloque génesis al blockchain
        blockchain.addBlock(genesisBlock);
    }

    private void addBlock(Transaction transaction) {
        // Obtener el hash del bloque anterior
        String previousHash = blockchain.get(blockchain.size() - 1).calculateHash();
        // Crear un nuevo bloque con la transacción y el hash del bloque anterior
        Block newBlock = new Block(previousHash, transaction);
        // Agregar el nuevo bloque al blockchain
        blockchain.addBl(newBlock);
    }


}
