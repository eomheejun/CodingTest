from collections import deque

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]


n = int(input())
r1,c1,r2,c2 = map(int,input().split())
visit = [[0]*n for i in range(n)]

def bfs(r1,c1,r2,c2):
    queue = deque()
    queue.append([r1,c1])
    while queue:
        x,y = queue.popleft()
        if x == r2 and y == c2:
            return visit[x][y]
        for  i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                queue.append([nx,ny])
                visit[nx][ny] = visit[x][y] +1
    return -1

print(bfs(r1,c1,r2,c2))
