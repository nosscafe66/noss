#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Create_Table_Tool"
__command__ = "python create_table.py test_tbl DDL.sql"

import sqlite3
import os
import sys

DB_NAME = "Kadai_DB"
FILE_PATH = "./sql/"

#引数取得
def arg_parse(*args:str) -> None:
    """
    sys.args[1]:作成テーブル名
    sys.args[2]:sqlファイル名
    """
    #print("=========Arg_Parse=========")
    if (len(sys.argv) -1 ) == 2:
        args1 = sys.argv[1]
        args2 = sys.argv[2]
        return args1,args2
    else:
      print("=========Arg_Parse_ERROR=========")
      sys.exit(1)

#実行DDLの作成
def get_query(FILE_PATH:str,args1:str,args2:str) -> None:
    """
    SQLファイルに変数を挿入してクエリを作成する
    Args:
    name(int);名前
    birthday(varchar(255))
    mailadress(varchar(255))
    tablename
    """
    #print("=========Get_Query=========")
    with open(os.path.join(FILE_PATH, args2), "r") as sql_file:
        return sql_file.read().format(table_name=args1)

#テーブル作成(DDLの読み込み)
def create_table(query:str,table_name:str,DB_NAME:str) -> str:
    """
    テーブル作成時のDDL文の例
    CREATE TABLE {tablename} (
        name INTEGER,
        birthday VARCHAR(255),
        mail_address VARCHAR(255)
    )
    """
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = 1")
    cur = conn.cursor()
    #Create_Table
    print(query)
    cur.execute(query)
    conn.commit()
    cur.execute('SELECT * FROM {}'.format(table_name))

#メイン処理
def main(*args) -> None:
    try:
      args1,args2 = arg_parse(sys.argv)
      query = get_query(FILE_PATH,args1,args2)
      create_table(query,args1,DB_NAME)
      sys.exit(0)
    except Exception as exceptmessage:
        print(exceptmessage)
        raise
      
if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])