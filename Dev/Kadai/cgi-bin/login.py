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

hash = password_hash.Hash(PASSWORD)
hash_pass=hash.get_hash()

DB_NAME = 'Kadai_DB'
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

#入力された情報から認証情報の問い合わせを実施
 #    user_id=cur.execute('SELECT id FROM user_table INNER JOIN auth_info_table ON user_table.id = auth_info_table.user_id WHERE id = {} AND {};'.format(LOGINID,hash_pass))
      
def get_authentication():
    user_id=cur.execute('SELECT id FROM user_table INNER JOIN auth_info_table ON user_table.id = auth_info_table.user_id WHERE id = {} ;'.format(LOGINID))
    password=cur.execute('SELECT password FROM user_table INNER JOIN auth_info_table ON user_table.id = auth_info_table.user_id WHERE password = {};'.format(hash_pass))

    if user_id == LOGINID and hash_pass == password:
        print("OK")
        sys.exit(1)
    else:
        print("Nothing")

if __name__ == "__main__":
    get_authentication()
