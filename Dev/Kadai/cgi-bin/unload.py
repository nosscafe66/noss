#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "File Unload"

import sqlite3
import sys

DB_NAME = 'Kadai_DB'

def table_search(*args):
    table_list=("account_table","test_tbl","test_tbl2")

TABLE_NAME=value
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
df_sql = pd.read_sql_query("select * from {}".format(TABLE_NAME), conn)
conn.close()

def main(*args):
    try:
      table_search(sys.argv[1])
    except Exception as exceptmessage:
      return
    
if __name__=="__main__":
    main(sys.argv[1])