n = int(input())
A = list(map(int,input().split()))
master, slave = map(int,input().split())

supervisor = len(A)

for i in range(len(A)):
    A[i] -= master
    if A[i]>0 and A[i]%slave ==0:
        supervisor+=A[i]//slave
    elif A[i]>0 and A[i]%slave:
        supervisor+=((A[i]//slave)+1)
    else:
        continue

print(supervisor)