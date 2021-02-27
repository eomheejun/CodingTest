from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

r,c = map(int,input().split())
map = []
visit = [[0]*c for _ in range(r)]
for i in range(r):
    map.append(list(input()))
water =deque()
for i in range(r):
    for j in range(c):
        if map[i][j] == 'S':
            start_x, start_y = i,j
        elif map[i][j] == 'D':
            end_x,end_y = i,j
        elif map[i][j] == '*':
            water.append([i,j])

def bfs(start_x,start_y,map):
    s = deque()
    s.append([start_x,start_y])
    visit[start_x][start_y] = 1
    while s:
        cnt = len(s)
        while cnt:
            x, y = s.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<r and 0<=ny<c:
                    if map[nx][ny] == '.' and visit[nx][ny]==0:
                        s.append([nx,ny])
                        visit[nx][ny] = visit[x][y]+1
                    elif map[nx][ny] == 'D':
                        return visit[x][y]
            cnt-=1
        Water()
    return "KAKTUS"



def Water():
    cnt = len(water)
    while cnt:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if map[nx][ny] == '.':
                    map[nx][ny] = '*'
                    water.append([nx, ny])
        cnt -= 1


Water()
print(bfs(start_x,start_y,map))