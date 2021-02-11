n = int(input())
data=set(list(map(int,input().split())))
m = int(input())
target = list(map(int,input().split()))
for i in target:
    if i in data:
        print(1)
    else:
        print(0)
