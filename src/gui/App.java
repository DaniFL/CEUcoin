package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class App extends JFrame{
    private JPanel mainPanel;
    private JPanel centerPanel, northPanel;
    private JLabel titleLabel, usernameLabel, passwordLabel, informativeLabel;
    private JTextField username, password;
    private JButton signUp, signIn;


    public App() {
        super("CEUCoin");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setSize(650, 650);
        setContentPane(mainPanel);

//        mainPanel.setBackground(Color.WHITE);
//        centerPanel.setBackground(Color.WHITE);
//        northPanel.setBackground(Color.WHITE);

        mainPanel.setBackground(Color.DARK_GRAY);
        centerPanel.setBackground(Color.DARK_GRAY);
        northPanel.setBackground(Color.DARK_GRAY);

        ImageIcon img = new ImageIcon("ceuLogo.png");
        setIconImage(img.getImage());

        signIn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Hello " + username.getText() +
                        " your password is: " + password.getText());
                UserDisplay userDisplay = new UserDisplay(App.this);
                userDisplay.pack();
                userDisplay.setVisible(true);
            }
        });

        signIn.setBackground(Color.DARK_GRAY);
        signUp.setBackground(Color.DARK_GRAY);
        signIn.setBorder(null);
        signUp.setBorder(null);
        username.setBorder(null);
        password.setBorder(null);

    }

    public static void main(String[] args) {
        App app = new App();
        app.pack();
        app.setVisible(true);
    }
}
