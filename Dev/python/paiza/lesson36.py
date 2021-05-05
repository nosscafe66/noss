d_1,d_2 = (int(x) for x in input().split())

if d_1 > 5:
    if d_2 > 5:
        print("10")
    if d_2 <= 5:
        print(5 + d_2)

elif d_1 <= 5:
    if d_2 > 5:
        print(d_1 + 5)
    if d_2 <= 5:
        print(d_1 + d_2)
        
elif d_2 <= 5:
    if d_1 <= 5:
        print(d_1 + d_2)
    elif d_1 > 5:
        print(5 + d_2)

elif d_2 > 5:
    if d_1 > 5:
        print("10")
    if d_1 <= 5:
        print(d_1 + d_2)
