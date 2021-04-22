from collections import deque
n = int(input())
data = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    a = ' '.join(input())
    b= a.split(' ')
    data.append(b)

visit = [[0]*n for i in range(n)]

cnt = 0


def bfs(x,y):
    que = deque()
    que.append([x, y])
    while que:
        a,b = que.popleft()
        tmp = data[a][b]
        for i in range(4):
            da = a+dx[i]
            db = b+dy[i]
            if 0<=da<n and 0<=db<n and visit[da][db] == 0 and data[da][db] == tmp:
                visit[da][db] = 1
                que.append([da,db])

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            cnt+=1

for i in range(n):
    for j in range(n):
        if data[i][j]=='R':
            data[i][j] = 'G'
visit = [[0]*n for i in range(n)]

cnt2=0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            cnt2+=1

print(cnt,cnt2)