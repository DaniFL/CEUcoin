import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Blockchain {
    private List<Block> chain;

    public Blockchain() {
        this.chain = new ArrayList<>();
        Transaction t = new Transaction("system", "system", 0);
        Block genesis = new Block(null, "genesis hash", t, LocalDateTime.now(), 3, 0);
        // mejor hacer un metodo statico genesis() en block y que devuelva el bloque genesis
        //chain.add(Block.genesis)
        chain.add(genesis);
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
