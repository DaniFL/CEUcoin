import java.util.ArrayList;
import java.util.List;

public class Block {
    private String previousHash;
    private List<Transaction> transactions;

    public Block(String previousHash) {
        this.previousHash = previousHash;
        this.transactions = new ArrayList<>();
    }

    public void addTransaction(Transaction transaction) {
        transactions.add(transaction);
    }

    public String calculateHash() {
        // Hay que poner la lógica de creación de hash para el bloque aquí
        return "blockHash";
    }

    public boolean isValid() {
        // Falta la lógica de verificación de integridad del bloque aquí
        return true;
    }
}
