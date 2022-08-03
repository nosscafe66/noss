#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Register BlogData"

import cgi, cgitb, sqlite3, codecs
import traceback
cgitb.enable()
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

DB_NAME = 'Kadai_DB'
QUERY_PATH= "./sql/Regist_data_insert.sql"
TABLE_NAME="blog_table"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

def register_data():
    cur.execute('INSERT INTO {} values(?, ?, ?, ?)'.format(TABLE_NAME),
                  (form["blog_id"].value,
                  form["blogtitle"].value,
                  form["article"].value,
                  form["created"].value))
    afterpage = codecs.open('./afterpage/after_blog.html', 'r', 'utf-8').read()
    print(afterpage)
    conn.commit()
    cur.close()
    conn.close()

def main():
  try:
    register_data()
  except Exception as exceptmessage:
    return

if __name__=="__main__":
    main()