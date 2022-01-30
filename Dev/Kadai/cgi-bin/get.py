#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "Get_Table & Serch Data"

import cgi, cgitb, sqlite3, codecs
cgitb.enable()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
form_check = 0

DB_NAME = 'Kadai_DB'
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute('SELECT * FROM account_table')
account_table_list = cur.fetchall()

result = '''
<table border="1">
<tr>
<th>Username</th>
<th>Birthday</th>
<th>Mailaddress</th>
</tr>
'''

for data in account_table_list:
    if form["username"].value in data:
        result += "<tr>"
        result += "<td>" + str(data[0]) + "</td>"
        result += "<td>" + str(data[1]) + "</td>"
        result += "<td>" + str(data[2]) + "</td>"
        result += "</tr>"
        afterpage = codecs.open('./afterpage/after.html', 'r', 'utf-8').read()
        afterpage = afterpage.replace('{% username %}', str(data[0]))
        afterpage = afterpage.replace('{% userinfo %}', str(data[1]))
        afterpage = afterpage.replace('{% result %}', result)
    elif not form["username"].value in data:
        result += "<tr>"
        result += "<td> Nothing Data </td>"
        result += "<td> Nothing Data </td>"
        result += "<td> Nothing Data </td>"
        result += "</tr>"
        afterpage = codecs.open('./afterpage/after.html', 'r', 'utf-8').read()
        afterpage = afterpage.replace('{% username %}', "Nothing Register")
        afterpage = afterpage.replace('{% userinfo %}', "Nothing Register")
        afterpage = afterpage.replace('{% result %}', result)

print(afterpage)
# conn.commit()
cur.close()
conn.close()