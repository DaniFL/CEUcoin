import java.security.*;
import java.time.LocalDate;
import java.util.Base64;

public class Transaction {
    public String sender;
    public String recipient;
    public double amount;
    private String signature;

    public LocalDate date;

    public Transaction(String sender, String recipient, double amount) {
        this.sender = sender;
        this.recipient = recipient;
        this.amount = amount;
        this.date = LocalDate.now();
    }

    @Override
    public String toString() {
        return "Transaction{" +
                "sender='" + sender + '\'' +
                ", recipient='" + recipient + '\'' +
                ", amount=" + amount +
                ", signature='" + signature + '\'' +
                ", date=" + date +
                '}';
    }
}
