import java.security.*;
import java.util.Base64;

public class Wallet {
    // Id de la tarjeta
    private double balance;
    private PublicKey publicKey;
    private PrivateKey privateKey;

    public Wallet(double v) {
        // Implementa la generación de claves públicas y privadas aquí
        KeyPair keyPair = generateKeyPair();
        this.publicKey = keyPair.getPublic();
        this.privateKey = keyPair.getPrivate();
    }

    public String getPublicKey() {
        return Base64.getEncoder().encodeToString(publicKey.getEncoded());
    }


    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            // Agregar una transacción al blockchain cada vez que se deposita
            Transaction transaction = new Transaction("system", "user", amount);
            addBlock(transaction);
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            // Agregar una transacción al blockchain cada vez que se retira
            Transaction transaction = new Transaction("user", "system", -amount);
            addBlock(transaction);
        }
    }

    public double getBalance() {
        return balance;
    }
}
