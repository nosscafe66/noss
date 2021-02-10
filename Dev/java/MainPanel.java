package javatest.panels;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

class MainPanel extends JPanel {
	JButton btn,btn2,btn3,btn4;
	JLabel paneltitle;
	JLabel wordregister;
	MainFrame mf;
	String str;
	public MainPanel(MainFrame m,String s){
		mf = m;
		str = s;
		this.setName("mp");
		this.setLayout(null);
		this.setSize(400, 600);
		
		JLabel paneltitle = new JLabel();
		paneltitle.setBounds(0, 5, 400, 40);

		this.add(paneltitle);
		btn = new JButton("用語登録画面に移動");
		btn.setBounds(70, 50, 150, 40);
		btn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				pc(mf.PanelNames[1]);
				JTextField wordregister = new JTextField(10);
				JPanel wordpanel = new JPanel();
				wordpanel.add(wordregister);
				String wordpane;
				wordpane  = JOptionPane.showInputDialog(null, "用語の入力", "入力画面",JOptionPane.PLAIN_MESSAGE);
			}
		});
		this.add(btn);

		btn2 = new JButton("用語検索画面に移動");
		btn2.setBounds(70, 100, 150, 40);
		btn2.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				pc(mf.PanelNames[2]);
				JTextField wordregister = new JTextField(10);
				JPanel wordpanel = new JPanel();
				wordpanel.add(wordregister);
				String wordpane;
				wordpane  = JOptionPane.showInputDialog(null, "用語の入力", "検索画面",JOptionPane.PLAIN_MESSAGE);
			}
		});
		this.add(btn2);

		btn3 = new JButton("辞書の使用方法画面に移動");
		btn3.setBounds(70, 150, 150, 40);
		btn3.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				pc(mf.PanelNames[3]);
			}
		});
		this.add(btn3);

		btn4 = new JButton("Logout");
		btn4.setBounds(70, 200, 150, 40);
		btn4.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				JLabel loglabel = new JLabel("Logout OK!");
				JOptionPane.showMessageDialog(null, loglabel);
			}
		});
		this.add(btn4);

	}
	public void pc(String str){
		mf.PanelChange((JPanel)this, str);
	}

	@Override
	public void pc(){
		JLabel loglabel = new Label("Logout OK!");
		JOptionPane.showMessageDialog(null, loglabel);
		//mf.PanelChange((JPanel)this, mf.PanelNames[0]);
	}
	
}