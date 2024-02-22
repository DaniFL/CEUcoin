import java.security.MessageDigest;
import java.time.LocalDate;

public class Block {
    private String previousHash;
    private Transaction transaction;
    private LocalDate time;
    //private Int index/heigth;
    private String hash;

    public Block(String previousHash, Transaction transaction) {
        this.previousHash = previousHash;
        this.transaction = transaction;
        this.time = LocalDate.now();
        this.hash = calculateHash();
    }

    public String calculateHash() {
        String dataToHash = previousHash + transaction.toString() + time.toString();
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

    public boolean isValid(String previousHash) {
        return this.previousHash.equals(previousHash) && this.hash.equals(calculateHash());
    }

    public String getHash() {
        return hash;
    }
}
