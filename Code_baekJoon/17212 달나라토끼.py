n = int(input())
coin = [1,2,5,7]
dp = [100001]*(n+1)
dp[0] = 0
for i in range(4):
    for j in range(coin[i],n+1):
        if dp[j-coin[i]] != 100001:
            dp[j] = min(dp[j],dp[j-coin[i]]+1)


print((dp[n]))