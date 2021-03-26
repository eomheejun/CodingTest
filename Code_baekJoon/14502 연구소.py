from itertools import combinations
import copy
n, m = map(int,input().split())
empty = []
graph = []
virus = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n):
  graph.append(list(map(int,input().split())))
  x = [i for i,j in enumerate(graph[i]) if j == 0]
  for j in x:
    empty.append([i,j])
  y = [i for i,j in enumerate(graph[i]) if j == 2]
  for j in y:
    virus.append([i,j])
copy_virus = copy.deepcopy(virus)
def bfs(build,tmp):
  while tmp:
    x,y = tmp.pop()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and build[nx][ny] == 0:
        tmp.append([nx,ny])
        build[nx][ny] = 2
  return build


tmp = combinations(empty,3)
tmp = list(tmp)

build = copy.deepcopy(graph)

cnt = []
a=0
for i in tmp:
  for j in i:
    build[j[0]][j[1]] = 1

  result = bfs(build,copy_virus)
  for x in range(n):
    a += result[x].count(0)
  cnt.append(a)
  a = 0
  build = copy.deepcopy(graph)
  copy_virus = copy.deepcopy(virus)

print(max(cnt))