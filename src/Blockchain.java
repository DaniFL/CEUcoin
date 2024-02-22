import java.util.ArrayList;
import java.util.List;

public class Blockchain {
    private List<Block> blocks;

    public Blockchain() {
        this.blocks = new ArrayList<>();
        // primer bloque génesis al inicio de la cadena
        blocks.add(new Block("0"));
    }

    public void addBlock(Block block) {
        // falta la lógica de agregado de bloques aquí
    }

    public boolean isValid() {
        // falta la lógica de verificación de integridad de la cadena aquí
        return true;
    }

    public Block getLatestBlock() {
        return blocks.get(blocks.size() - 1);
    }
}
