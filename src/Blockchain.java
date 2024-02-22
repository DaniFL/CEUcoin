import java.util.ArrayList;
import java.util.List;

public class Blockchain {
    private List<Block> chain;

    public Blockchain() {
        this.chain = new ArrayList<>();
        // primer bloque génesis al inicio de la cadena

    }

    public void addBlock(Block block) {
        chain.add(block);
    }

    public Block getLatestBlock() {
        return chain.get(chain.size() - 1);
    }
}
