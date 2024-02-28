package database;
import ceuCoin.Block;
import ceuCoin.Transaction;

import java.sql.*;
import java.text.SimpleDateFormat;
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
            String query = "CREATE TABLE IF NOT EXISTS Transaction (transaction_id INT PRIMARY KEY,\n" +
                    "    block_height REFERENCES Blocks(block_height) INT,\n" +
                    "    previous_hash VARCHAR(64),\n" +
                    "    current_hash VARCHAR(64),\n" +
                    "    timestamp TIMESTAMP,\n" +
                    "    difficulty INT,\n" +
                    "    nonce INT,\n" +
                    "    transaction_number INT,\n" +
                    "    amount DECIMAL(10, 2))";

            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.executeUpdate();
            query = "CREATE TABLE IF NOT EXISTS Block (block_height INT PRIMARY KEY,\n" +
                    "    previous_hash VARCHAR(64),\n" +
                    "    hash VARCHAR(64),\n" +
                    "    timestamp TIMESTAMP,\n" +
                    "    difficulty INT,\n" +
                    "    nonce INT)";
            PreparedStatement createTableStatement2 = connection.prepareStatement(query);
            createTableStatement2.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public boolean addBlock(Block block){
        String query = "INSERT INTO Block (block_height, previous_hash, current_hash, timestamp, difficulty, nonce, transaction_number, amount) \" +\n" +
                "                                 \"VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
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
