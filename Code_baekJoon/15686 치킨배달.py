from itertools import combinations

n, m = map(int,input().split())

data = []

home = []
chicken= []
for i in range(n):
  data.append(list(map(int,input().split())))
  if data[i].count(1):
    x = 1
    tmp = [i for i,j in enumerate(data[i]) if j==x]
    for k in tmp:
      home.append([i,k])
  if data[i].count(2):
    x = 2
    tmp = [i for i,j in enumerate(data[i]) if j==x]
    for k in tmp:
      chicken.append([i,k])

tmp = combinations(chicken,m)
tmp = list(tmp)

min_data = []
result =[]
sol = 0
for i in tmp:
  for j in home:
    for k in i:
      min_data.append(abs(k[0]-j[0])+abs(k[1]-j[1]))
    sol+=min(min_data)
    min_data=[]
  result.append(sol)
  sol=0

print(min(result))