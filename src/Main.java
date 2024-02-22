import java.util.ArrayList;
import java.util.List;

public class Main {
    private double balance;
    private List<Block> blockchain;

    public Main(double initialBalance) {
        this.balance = initialBalance;
        this.blockchain = new ArrayList<>();
        // Inicializar el blockchain con un bloque génesis
        initializeBlockchain();
    }

    private void initializeBlockchain() {
        // Crear el bloque génesis
        Block genesisBlock = new Block("0", new Transaction("genesis_sender", "genesis_recipient", 0));
        // Agregar el bloque génesis al blockchain
        blockchain.add(genesisBlock);
    }

    public double getBalance() {
        return balance;
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

    private void addBlock(Transaction transaction) {
        // Obtener el hash del bloque anterior
        String previousHash = blockchain.get(blockchain.size() - 1).calculateHash();
        // Crear un nuevo bloque con la transacción y el hash del bloque anterior
        Block newBlock = new Block(previousHash, transaction);
        // Agregar el nuevo bloque al blockchain
        blockchain.add(newBlock);
    }
}
