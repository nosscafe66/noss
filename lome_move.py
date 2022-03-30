# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "30 March 2022"
__prodactname__ = "Lome_Auto_Login"

#コマンド：python C:\Users\pltn\Desktop\work\mytool\lome_move.py 3 ファイル名 取得したい月

#Lome自動ログインRPA
import sys
import time
import pyautogui
import pyperclip
import requests
import webbrowser
from PIL import Image
from urllib.parse import urlparse
from urllib.request import urlopen

#lomeログインurlの設定
url = "https://lome.ft-cons.co.jp/ctrl/login"
webbrowser.open(url,new=1,autoraise=True) 

#ディスプレイのサイズを取得
DISPLAT_SIZE = pyautogui.size()
DISPLAT_WIDTH = DISPLAT_SIZE.width
DISPLAT_HEIGHT = DISPLAT_SIZE.height

#トリミング後の画像格納先
TRIMMED_FILE_DIR = "./trim_data"

#勤務表のスクショ画像ファイル名、勤務表のトップページファイル名(固定)
lome_kinmu = "lome_kinmu.png"
kinmu_hyou_top_page = "kinmu_hyou_top_page.png"

#ログインIDとパスワードを格納(iniファイルもしくはjsonファイルとしてkey:valueで社員情報を持たせる)
mail_address = "y_konosu@ft-cons.co.jp"
passwd = "nosscafe66"

#勤務表の画像の各種値の初期化
left = 10
right = 1900
bottom = 60

#lomeページのステータスコード確認
def request_page_check():
    session = requests.Session()
    response = session.get(url)
    http_status_code = response.status_code

    if http_status_code == 200:
        return session
    elif http_status_code != 200:
        sys.exit(1)
    else:
        sys.exit(1)

#lomeへの自動ログイン        
def login_site(mail_address:str,passwd:str) -> None:  
    time.sleep(1)
    #情報入力およびログイン処理まで
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyperclip.copy(mail_address)
    pyautogui.hotkey("command","v")
    pyautogui.press('tab')
    pyperclip.copy(passwd)
    pyautogui.hotkey("command","v")
    pyautogui.press('enter')
    return

#lomeのTopページから勤務表のページに遷移する処理(勤務表記載箇所のスクショを取得しクリック)
def get_top_url(DISPLAT_WIDTH:int,DISPLAT_HEIGHT:int) -> None:
    prtsc_range = (400, 380, 400, 50)
    prtsc = pyautogui.screenshot(lome_kinmu, region=prtsc_range)
    loc = pyautogui.locateOnScreen('lome_kinmu.png')
    center_loc = pyautogui.locateCenterOnScreen('lome_kinmu.png')
    pyautogui.click(loc)
    return

#勤務表のページ遷移後に全画面スクショ、月ごとの画像にトリミングする
def get_kinmu_hyou(countup:int,TRIMMED_FILE_DIR:str,kinmu_hyou_top_page:str,left:int,top:int,right:int,bottom:int) -> int:
    kinmu_hyou_top = pyautogui.screenshot(kinmu_hyou_top_page)
    picrange = (left,top,right,bottom)
    TRIMMED_FILE_DIR_FILE = "{}/_{}{}".format(TRIMMED_FILE_DIR,countup,kinmu_hyou_top_page)
    kinmu_hyou_top_trim = pyautogui.screenshot(TRIMMED_FILE_DIR_FILE,region=picrange)
    return

#コマンドライン引数で渡した数字をスクショ上からページを表示する
def set_kinmu_hyou(kinmu_hyou_month:int,TRIMMED_FILE_DIR:str,kinmu_hyou_top_page:str) -> int:
    TRIMMED_FILE_DIR_FILE = "{}/_{}{}".format(TRIMMED_FILE_DIR,kinmu_hyou_month,kinmu_hyou_top_page)
    loc = pyautogui.locateOnScreen(TRIMMED_FILE_DIR_FILE)
    pyautogui.click(loc)
    return

#lomeの出退勤情報をすべて取得する処理
def web_scraping(div_tag:str) -> str:
    response = requests.post()
    #div id="r_d_area" class="table"

#メイン処理
def main(kinmu_hyou_month:int) -> int:
    kinmu_hyou_month = sys.argv[1]
    try:
        session = request_page_check()
        login_site(mail_address,passwd)
        time.sleep(5)
        get_top_url(DISPLAT_WIDTH,DISPLAT_HEIGHT)
        time.sleep(5)
        top = 480
        for _ in range(1,10):
            get_kinmu_hyou(_,TRIMMED_FILE_DIR,kinmu_hyou_top_page,left,top,right,bottom)
            top = top + 65
            _ += 1
        time.sleep(5)
        set_kinmu_hyou(kinmu_hyou_month,TRIMMED_FILE_DIR,kinmu_hyou_top_page)
        
        session.close()
    except Exception as errormessage:
        print(errormessage)
        raise
    
if __name__ == "__main__":
    main(sys.argv)