package database;
import ceuCoin.Block;
import ceuCoin.Blockchain;
import ceuCoin.Transaction;

import java.sql.*;
import java.time.LocalDateTime;

public class JDBCManager {
    private static final String DATABASE_URL = "jdbc:sqlite:CEUCoinDB.db";
    static Connection connection = null;

    public JDBCManager(){
        try{
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection(DATABASE_URL);
            connection.createStatement().execute("PRAGMA foreign_keys=ON");
            System.out.println("Database connection opened.");

            this.creatTables();
        } catch (SQLException e){
            e.printStackTrace();
        } catch (ClassNotFoundException e){
            System.out.println("Libraries not loaded");
        }

    }

    private void creatTables() {

        try {
            Statement statement = connection.createStatement();
            String query;
            query = "CREATE TABLE IF NOT EXISTS Transaction (id INT,\n" +
                    "    block_height INT REFERENCES Block(height),\n" +
                    "    sender TEXT,\n" +
                    "    recipient TEXT,\n" +
                    "    amount DOUBLE,\n" +
                    "    datetime TIMESTAMP,\n" +
                    "    PRIMARY KEY (id AUTOINCREMENT))";

            statement.executeUpdate(query);

            query = "CREATE TABLE IF NOT EXISTS Block (height INT PRIMARY KEY,\n" +
                    "    previous_hash UNIQUE VARCHAR(64),\n" +
                    "    hash UNIQUE VARCHAR(64),\n" +
                    "    datetime TIMESTAMP,\n" +
                    "    difficulty INT,\n" +
                    "    nonce INT)";

            statement.executeUpdate(query);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addBlock(Block block) throws SQLException{

        String query = "INSERT INTO Block (height, previous_hash, hash, " +
                "datetime, difficulty, nonce) VALUES (?, ?, ?, ?, ?, ?)";

        PreparedStatement preparedStatement = connection.prepareStatement(query);
        preparedStatement.setInt(1, block.getHeight());
        preparedStatement.setString(2, block.getPreviousHash());
        preparedStatement.setString(3, block.getHash());
        preparedStatement.setObject(4, block.getDatetime());
        preparedStatement.setInt(5, block.getDifficulty());
        preparedStatement.setInt(6, block.getNonce());
        preparedStatement.executeUpdate();

        Transaction transaction = block.getTransaction();

        query = "INSERT INTO Transaction (block_height, sender, recipient, amount, datetime)" +
                "VALUES (?, ?, ?, ?, ?)";

        preparedStatement = connection.prepareStatement(query);
        preparedStatement.setInt(1, block.getHeight());
        preparedStatement.setString(2, transaction.getSender());
        preparedStatement.setString(3, transaction.getRecipient());
        preparedStatement.setDouble(4, transaction.getAmount());
        preparedStatement.setObject(5, transaction.getDatetime());
        preparedStatement.executeUpdate();
    }

    public Blockchain getBlockchain() throws SQLException{
        Blockchain blockchain = new Blockchain();
        Statement statement = connection.createStatement();
        String query = "SELECT * FROM Block";
        ResultSet resultSet = statement.executeQuery(query);
        while(resultSet.next()){
            int height = resultSet.getInt("height");
            String previousHash = resultSet.getString("previous_hash");
            String hash = resultSet.getString("hash");
            LocalDateTime datetime = (LocalDateTime) resultSet.getObject("datetime");
            int difficulty = resultSet.getInt("difficulty");
            int nonce = resultSet.getInt("nonce");
            Transaction transaction = getTransactionFromBlock(height);

            Block block = new Block(previousHash, hash, transaction, datetime, difficulty, nonce, height);
            blockchain.getChain().add(block);
        }
        resultSet.close();
        statement.close();

        return blockchain;
    }

    private Transaction getTransactionFromBlock(int block_height) throws SQLException{
        Statement statement = connection.createStatement();
        String query = "SELECT sender, recipient, amount, datetime FROM Transaction WHERE block_height = " + block_height;
        ResultSet resultSet = statement.executeQuery(query);
        String sender = resultSet.getString("sender");
        String recipient = resultSet.getString("recipient");
        double amount = resultSet.getDouble("amount");
        LocalDateTime dateTime = (LocalDateTime) resultSet.getObject("datetime");

        resultSet.close();
        statement.close();

        return new Transaction(sender, recipient, amount, dateTime);
    }

    public void disconnect() {
        try {
            connection.close();
            System.out.println("Database connection closed.");
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }


}
