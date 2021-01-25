from collections import deque

## 나이트의 이동 방향
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(start,end):
    ## deque 라이브러리 사용해서 큐 구현
     queue = deque()
     queue.append(start)

    #큐가 빌때까지 반복
     while queue:
         x,y = queue.popleft()

         ##현재위치가 목적지 와 같으면 리턴
         if x==end[0] and y==end[1]:
             return visit[x][y]

         ## 나이트의 8방향 위치 확인
         for i in range(8):
             nx = x + dx[i]
             ny = y + dy[i]

             ## 현재 위치가 필드 안에 있고 방문하지 않았다면
             if 0 <= nx < l and 0 <= ny < l and visit[nx][ny] ==0:

                    #큐에 현재 위치 넣고
                     queue.append((nx,ny))
                    #현재위치에 이전 위치값 +1 을 해준다.
                     visit[nx][ny] = visit[x][y]+1

test_case = int(input())

for i in range(test_case):
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    visit  = [[0]*l for i in range(l)]
    if start == end:
        print(0)
    else:
        print(bfs(start,end))

