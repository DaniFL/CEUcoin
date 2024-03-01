package ceuCoin;

import java.time.LocalDateTime;

public class Transaction {
    public String sender;
    public String recipient;
    public double amount;
    public LocalDateTime datetime;

    public Transaction(String sender, String recipient, double amount) {
        this.sender = sender;
        this.recipient = recipient;
        this.amount = amount;
        this.datetime = LocalDateTime.now();
    }

    public Transaction(String sender, String recipient, double amount, LocalDateTime datetime) {
        this.sender = sender;
        this.recipient = recipient;
        this.amount = amount;
        this.datetime = datetime;
    }

    public String getSender() { return sender; }
    public String getRecipient() { return recipient; }
    public double getAmount() { return amount; }
    public LocalDateTime getDatetime() { return datetime; }

    @Override
    public String toString() {
        return "ceuCoin.Transaction{" +
                "sender='" + sender + '\'' +
                ", recipient='" + recipient + '\'' +
                ", amount=" + amount +
                ", date=" + datetime +
                '}';
    }
}
