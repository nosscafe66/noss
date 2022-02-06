#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Register Signup Data"

import cgi, cgitb, sqlite3, codecs
import traceback
import datetime
import password_hash

cgitb.enable()
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

DB_NAME = 'Kadai_DB'
QUERY_PATH= "./sql/Regist_Signup_Data.sql"
USER_TABLE_NAME="user_table"
AUTH_USER_INFO="auth_info_table"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

now = datetime.datetime.now()
password = form["password"].value
hash = password_hash.Hash(password)
hash_pass=hash.get_hash()

def register_signup_data():
    now_str = datetime.datetime.now().strftime('%H:%M:%S.%f')
    cur.execute('INSERT INTO {} values(?, ?, ?, ?)'.format(USER_TABLE_NAME),
                  (form["userid"].value,
                  form["username"].value,
                  form["mailaddress"].value,
                  now_str))
    cur.execute('INSERT INTO {} values(?, ?, ?)'.format(AUTH_USER_INFO),
              (form["userid"].value,
              form["username"].value,
              hash_pass))
    afterpage = codecs.open('./afterpage/SignUp.html', 'r', 'utf-8').read()
    print(afterpage)
    conn.commit()
    cur.close()
    conn.close()

def main():
  try:
    register_signup_data()
  except Exception as exceptmessage:
    return

if __name__=="__main__":
    main()