import java.security.*;
import java.util.Base64;

public class Main {
    private double balance;
    //generamos bloques
    // inicializamos el blockchain
    // Hash del bloque anterior


    public Main(double initialBalance) {
        this.balance = initialBalance;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }
}
