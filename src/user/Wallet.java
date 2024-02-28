package user;

import ceuCoin.Transaction;

import java.security.*;

public class Wallet {
    private final String cardId;
    private double balance;
    public PublicKey publicKey;
    private PrivateKey privateKey;

    public Wallet(double balance, String id) {
        this.cardId = id;
        this.balance = balance;
    }

    public Transaction send(double amount, Wallet recipient) {
        Transaction transaction = null;
        if (balance > amount) {
            balance -= amount;
            recipient.receive(amount);
            // Agregar una transacción al blockchain cada vez que se deposita. Comprobar si mejor
            // una vez que se añada la transaccion al blockchain ahi recien debito y deposito el
            // dinero en las cuentas. Sino return exception "no se realizo la transaccion"
            transaction = new Transaction(cardId, recipient.getCardId(), amount);
        }
        return transaction;
    }

    public void receive (double amount) {
            balance += amount;
    }

    public double getBalance() {
        return balance;
    }

    public String getCardId(){
        return cardId;
    }
}
