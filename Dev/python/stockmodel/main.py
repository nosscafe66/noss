import configparser
import sys
import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import filedialog
import os
from tkinter.ttk import *
from PIL import Image, ImageTk

conf = configparser.ConfigParser()
conf_path = 'main.ini' if 1==len(sys.argv) else sys.argv[1]
conf.read(conf_path,encoding='cp932')

WINDOW_TITLE = conf.get('WINDOW','title')
WINDOW_WIDTH = conf.get('WINDOW','width')
WINDOW_HEIGHT = conf.get('WINDOW','height')
WINDOW_TEXT = conf.get('WINDOW','text')
BUTTON_TEXT1 = conf.get('BUTTON','text1')
BUTTON_TEXT2 = conf.get('BUTTON',"text2")
BUTTON_TEXT3 = conf.get('BUTTON',"text3")
BUTTON_TEXT4 = conf.get('BUTTON',"text4")
BUTOON_COLOR1 = conf.get('COLOR','color1')
BUTOON_COLOR2 = conf.get('COLOR','color2')

class MainWindow():
    def __init__(self):
        self.make_window = tk.Tk()
        self.make_window.geometry(str(WINDOW_WIDTH) +'x'+ str(WINDOW_HEIGHT))
        self.make_window.title(WINDOW_TITLE)
        self.make_window.wm_attributes("-topmost", True)
        self.make_window.wm_attributes("-transparent", True)
        self.make_window.config(bg='systemTransparent')
        

        frame = tk.Frame(self.make_window)
        frame.pack(fill="x")

        message = tk.Label(self.make_window,text=WINDOW_TEXT)
        message.pack()

        input_box1 = tk.Entry(self.make_window)
        input_box1.pack(fill="x")

        close_button = tk.Button(self.make_window,text=BUTTON_TEXT1,background="green",command=lambda: exit(self.make_window))
        close_button.pack(fill="x")

        run_button = tk.Button(self.make_window,text=BUTTON_TEXT2,background="green",command=self.func) 
        run_button.pack(fill="x")


        parse_button = tk.Button(self.make_window,text=BUTTON_TEXT3,bg='#f0e68c',command=self.scraping)
        parse_button.pack(fill="x")

        install_button = tk.Button(self.make_window,text=BUTTON_TEXT4,bg='#f0e68c',command=self.package_install)
        install_button.pack(fill="x")

        menu_bar = tk.Menu(self.make_window)
        self.make_window.config(menu=menu_bar)

        setting_file = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='File',menu=setting_file)

        setting_file.add_command(label='Environment_setting')
        setting_file.add_command(label='End')
        
        help_file = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='help',menu=help_file)

        help_file.add_command(label='FAQ')


        menu_bar.add_command(label='Open',command=self.open_file)
        menu_bar.add_separator()
        menu_bar.add_command(label='Close',command=self.close_disp)


    def open_file(self):
        pass
    

    def close_disp(self):
        pass

    def File_search(self):
        print("hello world")
        #subprocess.Popen(["python","search_file.py","py","./"])

    def exit(close_window):
        close_window.destroy()


    def package_install(self):
        install = subprocess.Popen(["./install.sh"])
        return install


    def func(self):
        #print("hello world")
        result = subprocess.Popen(["./stockmodel.sh"]) #["python","/Users/noss/Desktop/Dev/python_lesson/stockmodel.py"]
        return result


    def scraping(self):
        parse = subprocess.Popen(["python","scraping10.py"])
        return parse


    def main(self):
        self.make_window.mainloop()


if __name__ == "__main__":
    main = MainWindow()
    main.main()