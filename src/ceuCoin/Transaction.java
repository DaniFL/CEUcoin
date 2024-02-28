package ceuCoin;

import java.security.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Base64;

public class Transaction {
    public String sender;
    public String recipient;
    public double amount;
    public LocalDateTime date;

    public Transaction(String sender, String recipient, double amount) {
        this.sender = sender;
        this.recipient = recipient;
        this.amount = amount;
        this.date = LocalDateTime.now();
    }

    @Override
    public String toString() {
        return "ceuCoin.Transaction{" +
                "sender='" + sender + '\'' +
                ", recipient='" + recipient + '\'' +
                ", amount=" + amount +
                ", date=" + date +
                '}';
    }
}
