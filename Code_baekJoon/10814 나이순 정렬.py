n = int(input())
data = []
for i in range(n):
    data.append(input().split())
    data[i][0] = int(data[i][0])

data = sorted(data,key=lambda x:x[0])
for i in range(len(data)):
    data[i][0] = str(data[i][0])
    print(' '.join(data[i]))
