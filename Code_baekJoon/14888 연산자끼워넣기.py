from itertools import permutations

n = int(input())

a = list(map(int,input().split()))
data = list(map(int,input().split()))
tmp = []
i=0
op = ['a','b','c','d']
for i in range(4):
  x = [op[i]]*data[i]
  tmp.extend(x)

permute = set(permutations(tmp,len(tmp)))
permute = list(permute)
cnt = a[0]
result = []
for x in range(len(permute)):
  for y in range(len(permute[x])):
    if permute[x][y] == 'a':
      cnt += a[y+1]
    elif permute[x][y] == 'b':
      cnt -= a[y+1]
    elif permute[x][y] == 'c':
      cnt *= a[y+1]
    elif permute[x][y] == 'd':
      if cnt <= 0:
        cnt = -1 * (abs(cnt) // a[y+1])
      else:
        cnt //= a[y+1]
  result.append(cnt)
  cnt = a[0]

print(max(result))
print(min(result))

