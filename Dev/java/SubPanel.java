package javatest.panels;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

class SubPanel extends JPanel {
	JButton btn = new JButton("メインメニューへ移動");
	MainFrame mf;
	String str;
	public SubPanel(MainFrame m,String s){
		mf = m;
		str = s;
		this.setName(s);
		this.setLayout(null);
		this.setSize(400, 200);

		JLabel paneltitle = new JLabel();
		paneltitle.setBounds(50, 50, 50, 50);
		
		this.add(paneltitle);
		btn.setBounds(20, 20, 200, 50);
		btn.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				pc();
			}
		});
		this.add(btn);

	}
	public void pc(){
		mf.PanelChange((JPanel)this, mf.PanelNames[0]);
	}
}