import math
m,n = (int(x) for x in input().split())
s = m / n
s_1 = m % n
print(math.floor(s),end=" ")
print(s_1)
