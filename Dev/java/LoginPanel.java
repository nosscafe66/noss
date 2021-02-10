package javatest.panels;

import javax.swing.JButton;
import java.awt.Container;
import java.awt.BorderLayout;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.JOptionPane;
import java.awt.Color;
import javax.swing.JTextField;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class LoginPanel extends JPanel implements ActionListener  {

  
  public static JLabel userLabel;
  public static JTextField userText;
  public static JLabel passwordLabel;
  public static JPasswordField passwordText;
  public static JButton button;
  public static JLabel success;


  public static void main(String[] args) {
    
      JPanel panel = new JPanel();
      JFrame frame = new JFrame();

      frame.setSize(300, 300);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setVisible(true);
      frame.add(panel);

      panel.setLayout(null);

      userLabel = new JLabel("User");
      userLabel.setBounds(10 , 20 , 80 ,25);
      panel.add(userLabel);

      userText = new JTextField(20);
      userText.setBounds(100 , 20 , 165 , 25);
      panel.add(userText);

      passwordLabel = new JLabel("Password");
      passwordLabel.setBounds(10 , 50 ,80 ,25);
      panel.add(passwordLabel);

      passwordText = new JPasswordField();
      passwordText.setBounds(100, 50 ,165 ,25);
      panel.add(passwordText);

      button = new JButton("Login");
      button.setBounds(10 , 80 ,80, 25 );
      button.addActionListener(new LoginPanel());
      panel.add(button);
      
      success = new JLabel("");
      success.setBounds(10, 110 , 300 ,25);
      panel.add(success);

      frame.setVisible(true);

}


  @Override
    public void actionPerformed(ActionEvent e){
        String user = userText.getText();
        String password = passwordText.getText();


        if(user.equals("yuto") && password.equals("yuto1234")){
          success.setText("Login successful!");
          JLabel label = new JLabel("Login OK!");
          label.setForeground(Color.BLUE);
          JOptionPane.showMessageDialog(null, label);
           //pc(mf.PanelNames[0]);
        }

        else{
          success.setText("Login mistake!");
          JLabel label = new JLabel("One more pass");
          label.setForeground(Color.RED);
          JOptionPane.showMessageDialog(null, label);
         }
      }

      @Override
      public void pc(){
        mf.PanelChange((JPanel)this, mf.PanelNames[0]);
      }
    }