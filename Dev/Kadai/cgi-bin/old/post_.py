#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Post"

import sys
import os
import cgi
import cgitb
import io
import cgi, cgitb, sqlite3, codecs
cgitb.enable()
sys.path.append("../Kadai")
from insert_data import insert_data

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
cgitb.enable()
request_form = cgi.FieldStorage()

def validate_check():
    if 'username' not in request_form:
        print('Content-type: text/html; charset=UTF-8')
        print('')
        print('username フィールドが送信されていません。')
        sys.exit(1)

    username = request_form.getvalue('username', 'anonimus')
    birthday = request_form.getvalue('birthday', '*******')
    mailaddress = request_form.getvalue('mailaddress', '*******')
    password = request_form.getvalue('password','*******')
    print("Content-Type: text/html")
    print()
    htmlText = '''
    <!DOCTYPE html>
    <html>
        <head><meta charset="UTF-8" /></head>
    <body bgcolor="lightyellow">
        <h1>Regist!!</h1>
        <p><br/></p>
        <hr/>
        <a href="../index.html">back</a>
    </body>
    </html>
    '''
    print( htmlText.encode("cp932", 'ignore').decode('cp932') )
    #print('{} フィールドが送信されています。'.format(username))
    return username,birthday,mailaddress,password

table_name = "account_table"

def main() -> str:
    try:
        value1,value2,value3,value4 = validate_check()
        insert_data(value1,value2,value3,value4,table_name)
    except Exception as exeptmessage:
        raise
  
if __name__ == "__main__":
    main()