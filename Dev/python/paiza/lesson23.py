n = { 0:12 ,1:3 ,2:4 ,3:5 ,4:6 ,5:7 ,6:8 ,7:9 ,8:10 ,9:11 }
s = input()
s = s.replace("-","")
su = []
for i in s:
    if int(i) in n:
        M = n[int(i)] + n[int(i)]
        su.append(M)
print(sum(su))
