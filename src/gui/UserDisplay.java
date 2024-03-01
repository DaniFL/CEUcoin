package gui;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UserDisplay extends JFrame{
    private JPanel mainPanel;
    private JPanel actionPanel;
    private JButton balance;
    private JButton blockchain;
    private JButton contacts;
    private JPanel balancePanel;
    private JPanel blockchainPanel;
    private JPanel contactsPanel;
    private JLabel usernameLabel;
    private JLabel balanceLabel;
    private JLabel amount;

    public UserDisplay() {
        super("CEUCoin");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(450, 150, 450, 450);
        setContentPane(mainPanel);
        balance.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
//                blockchainPanel.setVisible(false);
//                contactsPanel.setVisible(false);
                balancePanel.setVisible(true);
            }
        });

        blockchain.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
//                contactsPanel.setVisible(false);
//                balancePanel.setVisible(false);
//                blockchainPanel.setVisible(true);
            }
        });
        contacts.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                balancePanel.setVisible(false);

            }
        });
    }

    public static void main(String[] args) {
        UserDisplay userDisplay = new UserDisplay();
        userDisplay.pack();
        userDisplay.setVisible(true);
    }
}
