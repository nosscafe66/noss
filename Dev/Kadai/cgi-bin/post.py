#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Register AccountData"

import cgi, cgitb, sqlite3, codecs
import traceback
cgitb.enable()
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

DB_NAME = 'Kadai_DB'
QUERY_PATH= "./sql/Regist_data_insert.sql"
TABLE_NAME="task_table"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
#with open(QUERY_PATH, "r") as sql_file:
#    value1="''" + form["username"].value + "''"
#    value2="''" + form["birthday"].value + "''"
#    value3="''" + form["mailaddress"].value + "''"
#    value4="''" + form["accountpass"].value + "''"
#    query = sql_file.read().format(column1=value1,column2=value2,column3=value3,column4=value4,table_name=TABLE_NAME)
#cur.execute(query)
def register_data():
    cur.execute('INSERT INTO {} values(?, ?, ?, ?)'.format(TABLE_NAME),
                  (form["date"].value,
                  form["username"].value,
                  form["mailaddress"].value,
                  form["task"].value))
    afterpage = codecs.open('./afterpage/RegisterData.html', 'r', 'utf-8').read()
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