from collections import deque

n = int(input())
a,b= map(int,input().split())
m = int(input())
data = [[0]*n for i in range(n)]
visit = [0]*n

## 연결된 그래프 생성
for i in range(m):
    x, y = map(int,input().split())
    data[x-1][y-1] = 1
    data[y-1][x-1] = 1

def bfs(data,start,visit):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in range(n):
            ##현재노드와 연결이 되있고 방문되지 않았다면 방문처리
            if data[v][i] == 1 and visit[i]==0:
                visit[i] = visit[v] +1
                queue.append(i)
    return visit
result = bfs(data,a-1,visit)

if result[b-1] == 0:
    print(-1)
else:
    print(result[b-1])