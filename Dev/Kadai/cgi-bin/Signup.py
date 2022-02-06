#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "User_Signup"


#パスワードをハッシュ値として保存するための処理を読み込む
import sys
from password_hash import password_hash
PASSWORD=sys.argv

def main():
  pass

if __name__=="__main__":
    run_pass_hash = password_hash.Hash()