N,M = (int(x) for x in input().split())

if N + M < 16:
    print("HIT")
elif N + M >= 16:
    print("STAND")
