d_n = []
for i in range(5):
    d = int(input())
    d_n.append(d)
    if d_n[i]-d_n[i-1] != 0:
        print(d_n[i]-d_n[i-1])
