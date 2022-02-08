#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Login"

import cgi, cgitb, sqlite3, codecs
import password_hash
import sys
cgitb.enable()

print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

LOGINID=form["loginid"].value
PASSWORD=form["password"].value

DB_NAME = 'Kadai_DB'

#入力された情報から認証情報の問い合わせを実施
 #    user_id=cur.execute('SELECT id FROM user_table INNER JOIN auth_info_table ON user_table.id = auth_info_table.user_id WHERE id = {} AND {};'.format(LOGINID,hash_pass))
 
def validation_check(LOGINID,PASSWORD):
    if not LOGINID or not PASSWORD:
        afterpage = codecs.open('./afterpage/loginfailed.html', 'r', 'utf-8').read()
        print(afterpage)
        sys.exit(1)
    else:
        return LOGINID,PASSWORD

def dict_factory(cursor, row):
   dic = {}
   for idx, col in enumerate(cursor.description):
       dic[col[0]] = row[idx]
   return dic

def get_authentication(PASSWORD):
    #user_id=cur.execute('SELECT password FROM user_table INNER JOIN auth_info_table ON user_table.id = auth_info_table.user_id WHERE password = ? ',[LOGINID])
    #password=cur.execute('SELECT password FROM user_table INNER JOIN auth_info_table ON user_table.id = auth_info_table.user_id WHERE password = ? ',[hash_pass])
    hash = password_hash.Hash(PASSWORD)
    hash_pass=hash.get_hash()
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_table INNER JOIN auth_info_table ON user_table.id = auth_info_table.user_id")
    user_info = cur.fetchone()
    
    if hash_pass in user_info["password"]:
        afterpage = codecs.open('./Top/index.html', 'r', 'utf-8').read()
        print(afterpage)
        conn.commit()
        cur.close()
        conn.close()
    
    else:
        afterpage = codecs.open('./afterpage/loginfailed.html', 'r', 'utf-8').read()
        print(afterpage)
        conn.commit()
        cur.close()
        conn.close()

if __name__ == "__main__":
    validation_check(LOGINID,PASSWORD)
    get_authentication(PASSWORD)