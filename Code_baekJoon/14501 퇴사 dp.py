n = int(input())

t = []
p = []
dp = [0]*(n+1)
for i in range(n):
  a, b = input().split()
  t.append(int(a))
  p.append(int(b))

for i in range(n):
  if t[i] <= n-i:
    dp[i+t[i]] = max(dp[i+t[i]],dp[i]+p[i])
  dp[i+1] = max(dp[i+1],dp[i])

print(dp[-1])