#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Get_CSV"

import cgi, cgitb, sqlite3, codecs
import csv
import datetime
cgitb.enable()

print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

DB_NAME = 'Kadai_DB'
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

account_table_list=cur.execute('SELECT * FROM account_table')
account_table_list = cur.fetchall()

now = datetime.datetime.now()
filename = './csv/account_list_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'

def make_file(account_table_list:str) -> str:
    for data in account_table_list:
      count=0
      now_str = datetime.datetime.now().strftime('%H:%M:%S.%f')
      print()
      with open(filename, 'a', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["{},{},{},{},{}".format(now_str,data[count],data[count+1],data[count+2],data[count+3])])

def download_csvfile(csvfile:str) -> str:
    afterpage = codecs.open('./afterpage/DataUnload.html', 'r', 'utf-8').read()
    afterpage = afterpage.replace('{% filename %}', str(csvfile))
    # conn.commit()
    #cur.close()
    #conn.close()
    return afterpage

def main():
    try:
      csvfile=make_file(account_table_list)
      afterpage=download_csvfile(csvfile)
      print(afterpage)
      cur.close()
      conn.close()
    except Exception as exceptmessage:
      print(exceptmessage)

if __name__=="__main__":
    main()