d_1,d_2,d_3 = (int(x) for x in input().split())

if d_1 >= d_2 :
    if d_1 >= d_3:
        print(d_1)
    elif d_3 >= d_1:
        print(d_3)
elif d_1 <= d_2:
    if d_2 >= d_3:
        print(d_2)
    elif d_3 >= d_2:
        print(d_3)
elif d_1 <= d_3:
    if d_2 >= d_3:
        print(d_2)
    elif d_3 >= d_2:
        print(d_3)
elif d_3 <= d_1:
    if d_2 >= d_1:
        print(d_2)
    elif d_1 >= d_2:
        print(d_1)
elif d_2 <= d_3:
    if d_1 >= d_3:
        print(d_1)
    elif d_3 >= d_1:
        print(d_3)
elif d_3 <= d_2:
    if d_2 >= d_1:
        print(d_2)
    elif d_1 >= d_2:
        print(d_1) 
