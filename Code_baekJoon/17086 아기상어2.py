from collections import deque

# 상어의 이동방향 8방향
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,-1,1,1,-1]


n , m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(tmp):
    queue = deque(tmp)
    while queue:
        x,y = queue.popleft()
        #상어가 있는 위치에서 8방향을 구한다.
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 8방향에 아무것도 없으면 현재 위치에서 1을 더한 값을 넣는다.
            # 상어의 다른 위치에서 최솟값을 구할 필요없이 8방향으로 현재 위치에서
            # 1을 더하면 최소가 된다.
            if 0 <= nx < n and 0 <= ny < m and  not graph[nx][ny]:
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
    return graph

##주어진 상어의 위치 좌표를 tmp 배열에 담아 bfs함수의 인자로 넣는다.
tmp = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            tmp.append([i,j])

## return 된 graph 값의 행중 max값을 뽑고 그값중 max값을 뽑아 -1 을 한다.
## 최초에 상어의 위치가 1로 표시되있기 때문
print(max(map(max, bfs(tmp)))-1)
