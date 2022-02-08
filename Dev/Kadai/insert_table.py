#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Insert_Table_Tool"
__command__ = "python insert_table.py data1.csv Insert_data.sql account_table"

from email import header
import sqlite3
import os
import sys
import csv

DB_NAME = "Kadai_DB"
FILE_PATH = "./sql/"
CSV_FILE = "./csv/" + sys.argv[1]

#引数取得
def arg_parse(*args:str) -> None:
    """
    sys.args[1]:csvファイル
    sys.args[2]:sqlファイル名
    sys.args[3]:テーブル名
    """
    #print("=========Arg_Parse=========")
    if (len(sys.argv) -1 ) == 3:
        args2 = sys.argv[2]
        args3 = sys.argv[3]
        return args2,args3
    else:
      print("=========Args_Parse_ERROR=========")
      sys.exit(1)

def get_query(CSV_FILE:str,args2:str,args3:str) -> None:
    print(CSV_FILE)
    if not CSV_FILE :
        print("=========Get_Query_ERROR=========")
        sys.exit(1)
    else:
        open_csv = open(CSV_FILE)
        read_csv = csv.reader(open_csv)

    #db接続
    #print("=========DB_CONNECT=========")
    conn = sqlite3.connect(DB_NAME)
    print("=========Get_Query=========")
    cur = conn.cursor()
    with open(os.path.join(FILE_PATH, args2), "r") as sql_file:
        return sql_file.read().format(table_name=args3),read_csv,open_csv
    
def insert_table(query:str,csv:str,open_csv:str) -> None:
    header = next(csv)
    rows = []
    for row in csv:
        rows.append(row)
        
    #db接続
    #print("=========DB_CONNECT=========")
    conn = sqlite3.connect(DB_NAME)
    print("=========Insert_Table=========")
    cur = conn.cursor()
    cur.executemany(query, rows)
    conn.commit()
    open_csv.close()

def main(*args) -> None:
    try:
        args2,args3 = arg_parse(sys.argv)
        query,csv,open_csv = get_query(CSV_FILE,args2,args3)
        insert_table(query,csv,open_csv)
    except Exception as exceptmessage:
        raise

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])