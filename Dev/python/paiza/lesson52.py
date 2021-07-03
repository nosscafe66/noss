n,s = input().split(" ")
length = n + s
if "km" in length:
    print(int(n) * 1000000)
elif "cm" in length:
    print(int(n) * 10)
else:
    print(int(n) * 1000)
