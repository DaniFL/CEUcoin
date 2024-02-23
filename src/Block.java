import java.security.MessageDigest;
import java.time.LocalDateTime;
import java.util.Date;
import java.time.LocalDate;

public class Block {
    public static final int MINE_RATE = 3000;
    private String previousHash;
    private String hash;
    private Transaction transaction;
    private LocalDateTime time;
    private int difficulty;
    private int nonce;


    public Block(String previousHash, String hash, Transaction transaction, LocalDateTime time, int difficulty, int nonce) {
        this.previousHash = previousHash;
        this.hash = hash;
        this.transaction = transaction;
        this.time = time;
        this.difficulty = difficulty;
        this.nonce = nonce;
    }

    private static String calculateHash(String previousHash, Transaction transaction, LocalDateTime time, int difficulty, int nonce) {
        String dataToHash = previousHash + transaction.toString() + time.toString() + String.valueOf(difficulty) + String.valueOf(nonce);
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = digest.digest(dataToHash.getBytes());
            StringBuilder hexString = new StringBuilder();
            for (byte hashByte : hashBytes) {
                String hex = Integer.toHexString(0xff & hashByte);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /*public boolean isValid(String previousHash) {
        return this.previousHash.equals(previousHash) && this.hash.equals(calculateHash());
    }*/

    public static Block mine(Block previousBlock, Transaction transaction){
        String previousHash = previousBlock.previousHash;
        int difficulty = previousBlock.difficulty;
        String hash = "";
        LocalDateTime time;
        int nonce = 0;

        do{
            nonce += 1;
            time = LocalDateTime.now();
            // si pasa menos de 3 segs (que es el mine rate y lo podemos cambiar) se aumenta
            // la dificultad de minar, sino se baja
            difficulty = previousBlock.time.plusSeconds(MINE_RATE).isAfter(time) ? difficulty + 1 : difficulty - 1;
            hash = calculateHash(previousHash, transaction, time, difficulty, nonce);
            // el hash va a ir cambiando hasta que encuentre la misma cantidad de
            // ceros al inicio, que la dificultad
        } while(hash.substring(0, difficulty).equals("0".repeat(difficulty)));

        return new Block(previousHash, hash, transaction, time, difficulty, nonce);
    }

    public String getHash() {
        return hash;
    }

    @Override
    public String toString() {
        return "Block{" +
                "previousHash='" + previousHash + '\'' +
                ", hash='" + hash + '\'' +
                ", transaction=" + transaction +
                ", time=" + time +
                ", difficulty=" + difficulty +
                ", nonce=" + nonce +
                '}';
    }
}
