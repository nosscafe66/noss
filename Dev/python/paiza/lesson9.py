count = 0
n = int(input())
while count <= n:
    count += 1
    if count == n:
        if count % 2 == 0:
            print("OFF")
            break
        elif count % 2 != 0:
            print("ON")
            break
