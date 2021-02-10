from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

m,n = map(int,input().split())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

def bfs():
    newlist = [[i, j] for i in range(n) for j in range(m) if data[i][j] == 1] #2차원 배열에서 '1'의 인덱스를 모두 찾는다
    que = deque()
    for i in range(len(newlist)):
        que.append(newlist[i])
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and data[nx][ny] == 0:
                que.append([nx,ny])
                data[nx][ny] = data[x][y]+1
    return data
result = bfs()
zero = [[i, j] for i in range(n) for j in range(m) if result[i][j] == 0]
if zero:
    print(-1)
else:
    print(max(map(max,result))-1)