package javatest.panels;

import javatest.panels.LoginPanel.LoginPanel;
import javax.swing.JFrame;
import javax.swing.JPanel;

class MainFrame extends JFrame{

public String[] PanelNames = {"mp","Sub1","Sub2","Sub3"/*,"Sub4"*/};
	MainPanel mp = new MainPanel(this,PanelNames[0]);
	SubPanel sp = new SubPanel(this,PanelNames[1]);
	SubPanel sp2 = new SubPanel(this,PanelNames[2]);
	SubSubPanel sp3 = new SubSubPanel(this,PanelNames[3]);
	//LoginPanel lp = new LoginPanel(this,PanelNames[4]);
	
	public  MainFrame(){
		this.add(mp);mp.setVisible(true);
		this.add(sp);sp.setVisible(false);
		this.add(sp2);sp2.setVisible(false);
		this.add(sp3);sp3.setVisible(false);
		//this.add(lp);lp.setVisible(true);
		this.setBounds(200, 200, 300, 300);
	}

	public static void main(String[] args) {
		MainFrame mf = new MainFrame();
		mf.setDefaultCloseOperation(EXIT_ON_CLOSE);
		mf.setVisible(true);
	}
	public void PanelChange(JPanel jp, String str){
	
		System.out.println(jp.getName());
		String name = jp.getName();
		if(name==PanelNames[0]){
			mp = (MainPanel)jp;
			mp.setVisible(false);
		}else if(name==PanelNames[1]){
			sp = (SubPanel)jp;
			sp.setVisible(false);
		}else if(name==PanelNames[2]){
			sp2 = (SubPanel)jp;
			sp2.setVisible(false);
		}else if(name==PanelNames[3]){
			sp3 = (SubSubPanel)jp;
			sp3.setVisible(false);
			LoginPanel.LoginPanel();
		}
		/*
		else if(name==PanelNames[4]){
			lp = (LoginPanel)jp;
			lp.setVisible(false);
		}
		*/
		if(str==PanelNames[0]){
			mp.setVisible(true);
		}else if(str==PanelNames[1]){
			sp.setVisible(true);
		}else if(str==PanelNames[2]){
			sp2.setVisible(true);
		}else if(str==PanelNames[3]){
			sp3.setVisible(true);
		}
		/*
		else if(str==PanelNames[4]){
			 lp.setVisible(true);
		}
		*/
	}
}