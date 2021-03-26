N, M = map(int, input().split(" "))

paperList = [list(map(int, input().split(" "))) for i in range(N)]
shapeList = [[[0, 1], [0, 2], [0, 3]], # ㅡ
             [[1, 0], [2, 0], [3, 0]], # ㅣ
             [[0, 1], [1, 0], [1, 1]], 
             [[1, 0], [2, 0], [2, 1]],
             [[1, 0], [2, 0], [2, -1]],
             [[0, 1], [0, 2], [1, 0]],
             [[0, 1], [0, 2], [1, 2]],
             [[0, 1], [1, 1], [2, 1]],
             [[0, 1], [1, 0], [2, 0]],
             [[0, 1], [0, 2], [-1, 2]],
             [[1, 0], [1, 1], [1, 2]],
             [[1, 0], [1, 1], [2, 1]],
             [[1, 0], [1, -1], [2, -1]],
             [[0, 1], [-1, 1], [-1, 2]],
             [[0, 1], [1, 1], [1, 2]],
             [[0, 1], [0, 2], [1, 1]],
             [[1, 0], [1, 1], [2, 0]],
             [[1, 0], [1, -1], [2, 0]],
             [[0, 1], [0, 2], [-1, 1]]]

max_sumary = 0
sumary = 0
for i in range(N):
    for j in range(M):
        for shape in shapeList:
            sumary = paperList[i][j]
            for k in range(3):
                nX = j + shape[k][1]
                nY = i + shape[k][0]
                if 0 <= nX <= M-1 and 0 <= nY <= N-1:
                    sumary += paperList[nY][nX]

            if(max_sumary < sumary):
                max_sumary = sumary

print(max_sumary)