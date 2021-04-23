n = int(input())

dp = [0] *(n+1)

dp[0] = 3
dp[1] = 7
dp[2] = 17

for i in range(3,n+1):
    dp[i] = (2*dp[i-1]+dp[i-2])%9901

print(dp[n-1])