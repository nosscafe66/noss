#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "File Unload"

import sqlite3
import sys
import datetime
import cgi, cgitb, sqlite3, codecs
cgitb.enable()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
form_check = 0

dt_now = datetime.datetime.now()

DB_NAME = 'Kadai_DB'
CSV_FILE = "./" + dt_now + "_unload.csv"

#table_list=("account_table","test_tbl","test_tbl2")#account ,などのテーブルのキーワードを受け取り検索ワードとして扱う。
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute('SELECT * FROM account_table')
account_table_list = cur.fetchall()
print(account_table_list)

with open (CSV_FILE,"w", encoding="utf-8") as f:
    for row in cur.execute('SELECT * FROM account_table;'):
        f.write(','.join([str(c) for c in row]) + '\n')
        afterpage = codecs.open('./afterpage/unload.html', 'r', 'utf-8').read()
        print(afterpage)
        conn.close()