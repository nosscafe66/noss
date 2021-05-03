N = int(input())
H,W = (int(x) for x in input().split())
Ans = (H * W) % N
print(Ans)
