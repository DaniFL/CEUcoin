import java.security.*;
import java.util.Base64;

public class Wallet {
    // Id de la tarjeta
    private PublicKey publicKey;
    private PrivateKey privateKey;

    public Wallet() {
        // Implementa la generación de claves públicas y privadas aquí
        KeyPair keyPair = generateKeyPair();
        this.publicKey = keyPair.getPublic();
        this.privateKey = keyPair.getPrivate();
    }

    public String getPublicKey() {
        return Base64.getEncoder().encodeToString(publicKey.getEncoded());
    }

    private KeyPair generateKeyPair() {
        try {
            KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
            keyPairGenerator.initialize(2048);
            return keyPairGenerator.generateKeyPair();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }

    public Transaction createTransaction(String recipient, double amount) {
        // Implementa la lógica de creación de transacciones aquí
        return new Transaction(getPublicKey(), recipient, amount);
    }
}
