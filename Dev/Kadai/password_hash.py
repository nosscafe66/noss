#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Password_Hash"

import hashlib
import sys

class Hash:
    def __init__(self,password:str) -> str:
        self.password = sys.argv[1]

    def main(password:str) -> str:
        pass_hash = hashlib.md5(password).hexdigest()
        return pass_hash

if __name__=="__main__":
    hash = Hash(sys.argv[1])
    hash.main = Hash(sys.argv[1])