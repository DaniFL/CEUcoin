import java.security.*;
import java.util.Base64;

public class Transaction {
    public String sender;
    public String recipient;
    public double amount;
    private String signature;

    public Transaction(String sender, String recipient, double amount) {
        this.sender = sender;
        this.recipient = recipient;
        this.amount = amount;
        this.signature = calculateSignature();
    }

    private String calculateSignature() {
        // Se puede usar java.security.Signature y java.security.KeyPairGenerator
        // para generar claves y firmar la transacción.
        return "signature";
    }

    // hacer funcion
    public boolean isValid() {
        // método que siempre devuelve true ya que queda implementar la lógica que compruebe el bloque válido
        // Implementa la lógica de verificación de la firma digital aquí
        return true;
    }
}
