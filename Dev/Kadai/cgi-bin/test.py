#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi

storage = cgi.FieldStorage()
print('Status: 200 OK')
print('Content-Type: text/html\n')

data = storage.getvalue('data')
recieve = data + "成功！"
print(recieve)