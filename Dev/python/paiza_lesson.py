# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

'''

    User{
    nickname : 名前
    old : 年齢
    birth : 誕生日
    state : 出身地
    }
    
'''
N = int(input())
for i in range(N):
    n_1,o_1,b_1,s_1 = input().split()
    print("User{")
    print("nickname : "+n_1)
    print("old : "+o_1)
    print("birth : "+b_1)
    print("state : "+s_1)
    print("}")
