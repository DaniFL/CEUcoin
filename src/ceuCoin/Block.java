package ceuCoin;

import java.security.MessageDigest;
import java.time.LocalDateTime;

public class Block {
    public static final long MINE_RATE = 4000;
    private String previousHash;
    private String hash;
    private Transaction transaction;
    private LocalDateTime datetime;
    private int difficulty;
    private int nonce;
    private final int height;


    public Block(String previousHash, String hash, Transaction transaction, LocalDateTime datetime, int difficulty, int nonce, int height) {
        this.previousHash = previousHash;
        this.hash = hash;
        this.transaction = transaction;
        this.datetime = datetime;
        this.difficulty = difficulty;
        this.nonce = nonce;
        this.height = height;
    }

    public static Block genesis(Transaction transaction){
        return new Block("undefined", "genesis hash", transaction, LocalDateTime.now(), 5, 0, 0);
    }

    private static String calculateHash(String previousHash, Transaction transaction, LocalDateTime datetime, int difficulty, int nonce, int height) {
        String dataToHash = previousHash + transaction.toString() + datetime.toString() + String.valueOf(difficulty) + String.valueOf(nonce) + String.valueOf(height);
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
        String previousHash = previousBlock.getHash();
        int difficulty = previousBlock.getDifficulty();
        // LocalDateTime prevTime = previousBlock.getDatetime();
        String hash = "";
        LocalDateTime datetime;
        int nonce = 0;
        int height = previousBlock.getHeight() + 1;

        do{
            nonce += 1;
            datetime = LocalDateTime.now();
            /*long timeElapsed = java.time.Duration.between(prevTime, time).getSeconds();
            // si pasa menos de 3 segs (que es el mine rate y lo podemos cambiar) se aumenta
            // la dificultad de minar, sino se baja
            //difficulty = timeElapsed < MINE_RATE ? difficulty + 1 : difficulty - 1;
            if (timeElapsed < MINE_RATE) {
                difficulty += 1; // Si los bloques se están minando muy rápido, aumenta la dificultad
            } else {
                difficulty -= 1; // Si los bloques se están minando muy lentamente, disminuye la dificultad
            }*/
            hash = calculateHash(previousHash, transaction, datetime, difficulty, nonce, height);
            // el hash va a ir cambiando hasta que encuentre la misma cantidad de
            // ceros al inicio, que la dificultad
        } while(!hash.startsWith("0".repeat(difficulty)));
//        !hash.substring(0, difficulty).equals("0".repeat(difficulty))
        return new Block(previousHash, hash, transaction, datetime, difficulty, nonce, height);
    }

    @Override
    public String toString() {
        return "ceuCoin.Block{" +
                "previousHash='" + previousHash + '\'' +
                ", hash='" + hash + '\'' +
                ", transaction=" + transaction +
                ", time=" + datetime +
                ", difficulty=" + difficulty +
                ", nonce=" + nonce +
                '}';
    }

    public String getPreviousHash() {
        return previousHash;
    }
    public String getHash() { return hash; }
    public Transaction getTransaction() {
        return transaction;
    }
    public LocalDateTime getDatetime(){ return datetime; }
    public int getDifficulty(){ return difficulty; }
    public int getNonce() { return nonce; }
    public int getHeight() { return height; }

}
