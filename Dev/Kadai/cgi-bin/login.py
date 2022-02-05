#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Get_CSV"

import cgi, cgitb, sqlite3, codecs
cgitb.enable()

print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

USERNAME=form["username"].value
PASSWORD=form["password"].value

DB_NAME = 'Kadai_DB'
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

#入力された情報から認証情報の問い合わせを実施
user_auth_query=cur.execute('SELECT * FROM user_table')
user_table_list = cur.fetchall()


print(USERNAME)
print(PASSWORD)