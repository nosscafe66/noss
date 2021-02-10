package javatest.panels;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JOptionPane;
import java.awt.Color;
import javax.swing.JButton;
import java.awt.BorderLayout;
import java.awt.Container;

class SubSubPanel extends SubPanel {
	public SubSubPanel(MainFrame m,String s){
		super(m,s);
		btn.setText("辞書の使用方法");
		JButton button1 = new JButton("OK");
		JButton button2 = new JButton();
		JPanel p = new JPanel();
    p.add(button1);
		p.add(button2);
	}
	@Override
	public void pc(){
		JLabel label = new JLabel("辞書の使い方");
		label.setForeground(Color.black);
		JOptionPane.showMessageDialog(null, label);
		mf.PanelChange((JPanel)this, mf.PanelNames[2]);
	}
}