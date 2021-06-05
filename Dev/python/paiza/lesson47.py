n = input()
if len(n) <= 2:
    if len(n) == 1:
        print("00" + str(n))
    elif len(n) == 2:
        print("0" + str(n))
elif len(n) == 3:
    print(n)
