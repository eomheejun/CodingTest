n = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))
total = 0
minv = 99999999999999999
for i in range(n-1):
    if i == 0:
        total += cost[0] * dist[0]
        minv = min(minv,cost[i])
    else:
        minv = min(minv,cost[i])
        total += minv*dist[i]

print(total)