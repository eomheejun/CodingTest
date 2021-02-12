import sys
sys.setrecursionlimit(5000)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))
cnt = 0
def dfs(x,y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == '1':
        graph[x][y] = '0'
        cnt+=1
        dfs(x - 1, y)  # 좌
        dfs(x, y - 1)  # 하
        dfs(x + 1, y)  # 우
        dfs(x, y + 1)  # 상
        return cnt
    return False

data = []
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            data.append(cnt)
            cnt = 0
print(len(data))
data.sort()
for i in data:
    print(i)