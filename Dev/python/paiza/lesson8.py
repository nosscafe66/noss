import math

N = int(input())
M = int(input())

a = N / M

if a == 0:
    print(round(a))
elif a != 0:
    print(math.floor(a))
