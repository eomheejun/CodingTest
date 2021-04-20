n, c = map(int,input().split())

data = list(map(int,input().split()))

start = sum(data)//c
end = sum(data)


while start<=end:
    mid = (start + end)//2
    cnt = 1
    blue = 0
    for i in range(n):
        blue += data[i]
        if blue>mid:
            cnt+=1
            blue = data[i]
    if cnt>c:
        start = mid+1
    else:
        result = mid
        end = mid-1

print(result)