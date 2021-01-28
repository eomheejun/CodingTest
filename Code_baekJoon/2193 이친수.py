n = int(input())
dp = [0]*91
dp[0] = 0
dp[1] = 1
dp[2] = 1
def binary_func(n):
    if n == 1 or n==2 :
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = binary_func(n-2)+binary_func(n-1)
    return dp[n]

print(binary_func(n))