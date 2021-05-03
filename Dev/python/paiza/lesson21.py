S = input()
n = ( "a", "e", "i", "o", "u" )
m = ( "A", "E", "I", "O", "U" )

for i in n:
    S = S.replace(str(i),"")
    for j in m:
        S = S.replace(str(j),"")
print(S)
