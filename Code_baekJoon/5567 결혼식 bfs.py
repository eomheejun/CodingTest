from collections import deque

n = int(input())
m = int(input())

graph = [[0]*n for i in range(n)]
visit = [0]*n
visit[0] = 1
for i in range(m):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1


def bfs():
    que = deque()
    que.append(0)
    while que:
        v = que.popleft()
        for i in range(n):
            if graph[v][i] == 1 and visit[i]==0:
                visit[i] = visit[v]+1
                que.append(i)

    return visit

a = bfs()
cnt = 0
for i in a:
    if 1<i<=3:
        cnt+=1
print(cnt)