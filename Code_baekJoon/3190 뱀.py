from collections import deque
n = int(input())
k = int(input())
position = []
dx =[1,-1,0,0]
dy =[0,0,1,-1]
graph = [[0]*n for i in range(n)]
graph[0][0] = 1

for i in range(k):
  position.append(list(map(int,input().split())))
  graph[position[i][0]-1][position[i][1]-1] = 'apple'

cnt = int(input())
info = []
time = []
for i in range(cnt):
  info.append(list(input().split()))
  info[i][0] = int(info[i][0])
  time.append(info[i][0])


second = -1
q = deque()
q.append([0,0])
ddx = dx[2]
ddy = dy[2]
tail = deque()
tail.append([0,0])
while q:
  second +=1
  x,y = q.popleft()
  if second in time:
    if info[time.index(second)][1] == 'D':
      if ddx == dx[2] and ddy == dy[2]:
        ddx = dx[0]
        ddy = dy[0]
      elif ddx == dx[0] and ddy == dy[0]:
        ddx = dx[3]
        ddy = dy[3]
      elif ddx == dx[1] and ddy == dy[1]:
        ddx = dx[2]
        ddy = dy[2]
      elif ddx == dx[3] and ddy == dy[3]:
        ddx = dx[1]
        ddy = dy[1]
    elif info[time.index(second)][1] == 'L':
      if ddx == dx[2] and ddy == dy[2]:
        ddx = dx[1]
        ddy = dy[1]
      elif ddx == dx[0] and ddy == dy[0] :
        ddx = dx[2]
        ddy = dy[2]
      elif ddx == dx[1] and ddy == dy[1]:
        ddx = dx[3]
        ddy = dy[3]
      elif ddx == dx[3] and ddy == dy[3]:
        ddx = dx[0]
        ddy = dy[0]
  nx = x+ddx
  ny = y+ddy
  if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1:
    q.append([nx,ny])
    if graph[nx][ny] != 'apple':
      a,b = tail.popleft()
      graph[a][b] = 0
      graph[nx][ny] = 1
      tail.append([nx,ny])
    else:
      tail.append([nx,ny])
      graph[nx][ny] = 1
  else:
    break



print(second+1)