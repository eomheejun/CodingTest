C,N=map(int,input().split())
a=[]
dp=[100001]*1001
dp[0] = 0

for i in range(N):
    a.append(list(map(int,input().split())))
    dp[a[i][1]] = a[i][0]

for i in range(1, C+1):
    for j in range(N):
        start = i - a[j][1]
        if start < 0:
            start = 0
        dp[i] = min(dp[start] + a[j][0], dp[i] )

print(dp[C])
