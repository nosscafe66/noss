xc,yc,r_1,r_2 = (int(x) for x in input().split())
n = int(input())
for i in range(n):
    x_n,y_n = (int(x) for x in input().split())
    #print(x_n,y_n)
    if r_1 ** 2 <= (x_n - xc) ** 2 + (y_n - yc) ** 2 <= r_2 ** 2:
        print("yes")
    elif not (r_1 ** 2 <= (x_n - xc) ** 2 + (y_n - yc) ** 2 <= r_2 ** 2):
        print("no")
