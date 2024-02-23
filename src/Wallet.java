import java.security.*;
import java.util.Base64;

public class Wallet {
    // Id de la tarjeta
    private final String id;
    private double balance;
    private PublicKey publicKey;
    private PrivateKey privateKey;

    public Wallet(double balance, String id) {
        this.id = id;
        this.balance = balance;
    }

    public Transaction send(double amount, String recipient) {
        Transaction transaction = null;
        if (balance > amount) {
            balance -= amount;
            // Agregar una transacción al blockchain cada vez que se deposita
            transaction = new Transaction(id, recipient, amount);
        }
        return transaction;
    }

    public void receive (double amount) {
            balance += amount;
    }

    public double getBalance() {
        return balance;
    }

    public String getId(){
        return id;
    }
}
