#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Insert_Data"

DB_NAME = "Kadai_DB"
query_path = "./sql/Regist_data_insert.sql"

import sys
import os
import sqlite3

def insert_data(value1,value2,value3,value4,value5) -> None:
  try:
    print(value1,value2,value3,value4,value5)
    #db接続
    #print("=========DB_CONNECT=========")
    conn = sqlite3.connect(DB_NAME)
    print("=========Insert_Table=========")
    
    with open(query_path, "r") as sql_file:
        query = sql_file.read().format(value1,value2,value3,value4,table_name=value5)#column1=value1,column2=value2,column3=value3,column4=value4,table_name=value5
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
  except Exception as exceptmessage:
    print(exceptmessage)
    raise

if __name__ == "__main__":
    insert_data(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])