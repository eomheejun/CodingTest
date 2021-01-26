from collections import deque

num = int(input())
n = int(input())
network = [[0]*num for i in range(num)]
for i in range(n):
    x, y = map(int,input().split())
    network[x-1][y-1] = 1
    network[y-1][x-1] = 1


def bfs(network,v):
    ## 현재 위치를 queue와 connect에 넣는다.
    queue = deque([v])
    connect = [v]
    ## queue 없을때까지 반복
    while queue:
        v = queue.popleft()
        # 존재하는 컴퓨터 수만큼 for문을 돌린다.
        for i in range(num):
            ## 현재 시점과 연결된 노드만 connect에 담는다.
            if network[v][i] == 1 and i not in connect:
                connect.append(i)
                queue.append(i)
    return len(connect)-1

print(bfs(network,0))