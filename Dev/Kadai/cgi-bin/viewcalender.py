#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "ViewCalender"

import cgi, cgitb, sqlite3, codecs
import sys
cgitb.enable()
print("Content-Type: text/html")
print()
form = cgi.FieldStorage()
form_check = 0

def main():
    zero,one,two,three,four,five,six,seven,eight,nine,m,a,p,sep,form = [[0,1,1,1,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]],[[0,0,1,0,0],[0,1,1,0,0],[1,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1]],[[0,1,1,1,0],[1,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,1,1,1,1]],[[1,1,1,1,0],[0,0,0,0,1],[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,0]],[[1,0,0,0,0],[1,0,0,0,0],[1,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]],[[1,1,1,1,1],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]],[[0,1,1,1,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,0],[1,0,0,0,1],[0,1,1,1,0]],[[1,1,1,1,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]],[[0,1,1,1,0],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,1,1,0]],[[0,1,1,1,0],[1,0,0,0,1],[0,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,1,1,1,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1]],[[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,0,1,0],[1,1,1,1,0],[1,0,0,1,0]],[[0,0,0,0,0],[1,1,1,1,0],[1,0,0,1,0],[1,1,1,1,0],[1,0,0,0,0],[1,0,0,0,0]],[[0,0,0,0,0],[0,0,2,0,0],[0,0,2,0,0],[0,0,0,0,0],[0,0,2,0,0],[0,0,2,0,0]],'%Y-%m-%d %H:%M %p'
    digdict_ = {str(i):v for i,v in enumerate([zero,one,two,three,four,five,six,seven,eight,nine])}
    alpdict_ = {'a':a,'m':m,'p':p,':':sep}
    all_dict = {**digdict_,**alpdict_}
    now = __import__('datetime').datetime.now()
    from time import strftime
    #print('It may not work\n')
    #print(f"Today is {now.year}-{now.month}-{now.day} \n")
    lh = ((int(strftime('%H'))-3+24))%24
    h,m= '00'+str(lh), '00'+strftime('%M')
    ftime = f"{int(h[-2])}{int(h[-1])}:{int(m[-2])}{int(m[-1])}"
    hours,mins = str(int(now.hour)-4), str(now.minute)
    meridiem = now.strptime(f'{hours}','%H').strftime('%I %p').split(' ')
    #full_time = f'{ftime}{meridiem[1].lower()}'
    afterpage = codecs.open('./admin/index.html', 'r', 'utf-8').read()
    print(afterpage)
    [print(__import__('calendar',fromlist=[None]).month(now.year,now.month,4))]
main()