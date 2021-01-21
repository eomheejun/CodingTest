import math
T = int(input())


def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

data = []
for i in range(T):
    data.append(list(map(int,input().split())))

for i,j in data:
    print(nCr(j,i))

