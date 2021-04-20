n, c = map(int,input().split())

data = []

for i in range(n):
    data.append(int(input()))

data.sort()

start = 1
end = data[-1] - data[0]

while start<=end:
    now = data[0]
    mid = (start + end)//2
    cnt = 1
    for i in range(1,n):
        if data[i] - now >= mid:
            cnt+=1
            now = data[i]
    if cnt >= c:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)