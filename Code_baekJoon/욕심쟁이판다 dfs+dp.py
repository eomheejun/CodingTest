import sys

sys.setrecursionlimit(100000)
n = int(input())
data = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    data.append(list(map(int,input().split())))

visit = [[0]*n for i in range(n)]

def dfs(x,y):
    if visit[x][y]:
        return visit[x][y]

    visit[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and data[x][y]<data[nx][ny]:
            visit[x][y] = max(visit[x][y], dfs(nx,ny)+1)
    return visit[x][y]


result = 1
for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))

print(result)