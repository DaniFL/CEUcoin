package gui;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class App extends JFrame{
    private JPanel mainPanel;
    private JPanel westPanel;
    private JPanel southPanel;
    private JPanel eastPanel;
    private JPanel northPanel;
    private JLabel usernameLabel;
    private JLabel passwordLabel;
    private JLabel titleLabel;
    private JTextField username;
    private JPasswordField password;
    private JButton signUp;
    private JButton signIn;


    public App() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(450, 150, 450, 450);
        setContentPane(mainPanel);

        signIn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Hello " + username.getText() +
                        " your password is: " + password.getText());
            }
        });

//        Image img = new ImageIcon(this.getClass().getResource("/ceuLogo.png")).getImage();
//        icon.setIcon(new ImageIcon(img));
    }

    public static void main(String[] args) {
        App app = new App();
        app.pack();
        app.setVisible(true);
    }
}
