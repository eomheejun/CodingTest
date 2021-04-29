from collections import deque


def solution(n, computers):
    if n == 1:
        return 1

    que = deque()
    visit = [0] * n
    que.append(0)
    cnt = 0
    def bfs(x):
        que.append(x)
        while que:
            x = que.popleft()
            for i in range(n):
                if computers[x][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    while visit.count(0)>=1:
        bfs(visit.index(0))
        cnt+=1
    return cnt

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n,computers))