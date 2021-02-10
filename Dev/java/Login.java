

import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.Container;
import java.awt.BorderLayout;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.JOptionPane;
import java.awt.event.*;
import java.awt.Color;



public class Login implements ActionListener {

  
  private static JLabel userLabel;
  private static JTextField userText;
  private static JLabel passwordLabel;
  private static JPasswordField passwordText;
  private static JButton button;
  private static JLabel success;

  public static void main(String[] args){
      JPanel panel = new JPanel();
      JFrame frame = new JFrame();
      
      frame.setSize(350, 350);
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
      button.addActionListener(new Login());
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
        //System.out.println(user + "," + password);

        if(user.equals("yuto") && password.equals("yuto1234")){
          success.setText("Login successful!");

          int g = -1;
          while(g < 0){
           if(input.length() > 0){
             g++;
             System.out.println("Thank you");

             
           }
           

           else{
             System.out.println("Enter your name");
            }
          }



        }else{
          /* 
          success.setText("one more");
          JLabel label = new JLabel("Message");
            label.setForeground(Color.RED);
            JOptionPane.showMessageDialog(this , label);
            */
            int t = -1;
            while(t < 0){
             if(login.length() > 0){
               t++;
               System.out.println("Thank you");
             }else{
               System.out.println("Enter your name");
              }
          }
    }
    
  }


}