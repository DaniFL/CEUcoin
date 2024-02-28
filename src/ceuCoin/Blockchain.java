import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Blockchain {
    private final List<Block> chain;

    public Blockchain() {
        this.chain = new ArrayList<Block>();
        Transaction t = new Transaction("system", "system", 0);
        chain.add(Block.genesis(t));
        System.out.println(chain);
    }

    public void addBlock(Transaction transaction) {
        Block newBlock = Block.mine(this.getLatestBlock(), transaction);
        chain.add(newBlock);
    }

    public Block getLatestBlock() {
        return chain.get(chain.size() - 1);
    }

    @Override
    public String toString() {
        return "Blockchain{" +
                "chain=" + chain +
                '}';
    }
}
