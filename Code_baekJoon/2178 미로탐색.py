from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
visit = [[False]*m for i in range(n)]
visit[0][0] = True
def bfs(n,m):
    queue = deque()
    queue.append([0, 0])
    while queue:
        x,y = queue.popleft()
        if x == (n-1) and y==(m-1):
            return graph[n-1][m-1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == '1' and visit[nx][ny] == False:
                queue.append([nx,ny])
                visit[nx][ny] = True
                graph[nx][ny] = int(graph[x][y])+1
    return graph[n-1][m-1]



print(bfs(n,m))
