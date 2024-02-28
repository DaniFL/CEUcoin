package database;
import java.sql.*;
import java.text.SimpleDateFormat;
public class JDBCManager {
    private static final String DATABASE_URL = "jdbc:sqlite:CEUCoinDB.db";
    static Connection connection = null;

    public static Connection establishConnection() {

        try {
            connection = DriverManager.getConnection(DATABASE_URL);
            //Patient table is created if it does not exist
            String createTableQuery1 = "CREATE TABLE IF NOT EXISTS Transaction (transaction_id INT PRIMARY KEY,\n" +
                    "    block_id REFERENCES Blocks(block_id) INT,\n" +
                    "    previous_hash VARCHAR(64),\n" +
                    "    current_hash VARCHAR(64),\n" +
                    "    timestamp TIMESTAMP,\n" +
                    "    difficulty INT,\n" +
                    "    nonce INT,\n" +
                    "    transaction_number INT,\n" +
                    "    amount DECIMAL(10, 2))";
            PreparedStatement createTableStatement1 = connection.prepareStatement(createTableQuery1);
            createTableStatement1.executeUpdate();
            String createTableQuery2 = "CREATE TABLE IF NOT EXISTS Blocks ( block_id INT PRIMARY KEY,\n" +
                    "    previous_hash VARCHAR(64),\n" +
                    "    timestamp TIMESTAMP,\n" +
                    "    difficulty INT,\n" +
                    "    nonce INT)";
            PreparedStatement createTableStatement2 = connection.prepareStatement(createTableQuery2);
            createTableStatement2.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return connection;
    }

    public boolean insertTransaction(, String password, Patient patient) {
        try {
            // Insert new patient into the database
            String insertQuery = "INSERT INTO Transactions (block_id, previous_hash, current_hash, timestamp, difficulty, nonce, transaction_number, amount) \" +\n" +
                    "                                 \"VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
            PreparedStatement insertStatement = connection.prepareStatement(insertQuery, Statement.RETURN_GENERATED_KEYS);
            insertStatement.setString(1, username);
            insertStatement.setString(2, password);

            int rowsAffected = insertStatement.executeUpdate();

            if (rowsAffected > 0) {
                // Retrieve the auto-generated patient_id
                ResultSet generatedKeys = insertStatement.getGeneratedKeys();

                if (generatedKeys.next()) {
                    int patient_id = generatedKeys.getInt(1);

                    // Now insert data into patient_data table
                    String insertDataQuery = "INSERT INTO patient_data (patient_id, name, surname, birthday, gender, clinicalHistory, password) VALUES (?, ?, ?, ?, ?, ?, ?)";
                    PreparedStatement dataInsertStatement = connection.prepareStatement(insertDataQuery);
                    dataInsertStatement.setInt(1, patient_id);
                    dataInsertStatement.setString(2, patient.getName());
                    dataInsertStatement.setString(3, patient.getSurname());

                    // Convert Client.Date to 'YYYY-MM-DD' format
                    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
                    String formattedDate = dateFormat.format(patient.getBirthday());
                    dataInsertStatement.setString(4, formattedDate);

                    dataInsertStatement.setString(5, patient.getGender().toString());
                    dataInsertStatement.setString(6, patient.getClinicalHistory().toString());
                    dataInsertStatement.setString(7, password);

                    int dataRowsAffected = dataInsertStatement.executeUpdate();

                    return dataRowsAffected > 0;
                }
            }

            return false;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public boolean authenticatePatient(String username, String password) {
        try {
            // Verify if the patient is in the database
            String query = "SELECT * FROM patient p JOIN patient_data pd ON p.patient_id = pd.patient_id WHERE p.username = ? AND pd.password = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, username);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next();
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }


}
