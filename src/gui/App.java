package gui;

import javax.swing.*;
import java.awt.*;
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
        super("CEUCoin");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        setResizable(false);
        this.setSize(420, 420);
        setContentPane(mainPanel);
        ImageIcon img = new ImageIcon("ceuLogo.png");
        setIconImage(img.getImage());

        signIn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Hello " + username.getText() +
                        " your password is: " + password.getText());
            }
        });

    }

    public static void main(String[] args) {
        App app = new App();
        app.pack();
        app.setVisible(true);
    }
}
