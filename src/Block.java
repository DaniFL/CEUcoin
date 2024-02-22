import java.util.ArrayList;
import java.util.List;

public class Block {
    private String previousHash;
    private Transaction transaction;

    public Block(String previousHash, Transaction transaction) {
        this.transaction = transaction;
        //transaccion aqui
    }

    public void addTransaction(Transaction transaction) {
        transaction.add(transaction);
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
