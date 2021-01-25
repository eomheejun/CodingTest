import sys
sys.setrecursionlimit(5000)

t = int(input())
for i in range(t):
    ## 가로길이 m 세로길이 n 배추 심어진곳 k
    m,n,k = map(int,input().split())

    ## 배추가 심어진 곳을 1로 안심어진곳을 0으로

    field = [[0]*m for i in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        field[y][x] = 1

    def dfs(x,y):
        # 범위 벗어나면 False
        if x<=-1 or x>=n or y<=-1 or y>=m:
            return False

        #배추가 심어진 곳이면 0으로 바꾸고 상하좌우 모두 재귀적으로 호출
        if field[x][y] == 1:
            field[x][y] = 0
            dfs(x-1,y) #좌
            dfs(x,y-1) #하
            dfs(x+1,y) #우
            dfs(x,y+1) #상
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    print(result)
