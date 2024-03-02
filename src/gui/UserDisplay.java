package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UserDisplay extends JFrame{
    private JPanel mainPanel, actionPanel;
    private JButton balance, blockchain, contacts;
    private JPanel balancePanel;
    private JLabel usernameLabel, balanceLabel, amountLabel;

    public UserDisplay(JFrame App) {
        super("CEUCoin");
        App.setVisible(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setContentPane(mainPanel);

        mainPanel.setBackground(Color.GRAY);
        balancePanel.setBackground(Color.GRAY);
        actionPanel.setBackground(Color.DARK_GRAY);

        balance.setBackground(Color.DARK_GRAY);
        balance.setBorder(null);

        blockchain.setBackground(Color.DARK_GRAY);
        blockchain.setBorder(null);

        contacts.setBackground(Color.DARK_GRAY);
        contacts.setBorder(null);


    }
}
