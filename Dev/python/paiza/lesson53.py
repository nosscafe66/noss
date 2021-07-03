N = int(input())
A = []
for i in range(1,8):
    A.append(int(input()))
if sum(A) < N:
    print(sum(A))
elif sum(A) > N:
    print(N)
