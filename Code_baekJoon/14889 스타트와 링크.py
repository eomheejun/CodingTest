from itertools import combinations

n = int(input())
data = []
mem =[]
for i in range(n):
  mem.append(i+1)
  data.append(list(map(int,input().split())))

tmp = (combinations(mem,len(mem)//2))
tmp = list(tmp)
score_team2 = 0
result = []

for i in range(len(tmp)//2):
  team = tmp[i]
  score_team1 = 0
  for j in range(n//2):
    member = team[j]
    for k in team:
      score_team1 += data[member-1][k-1]

  team = tmp[-i-1]
  score_team2 = 0
  for j in range(n//2):
    member = team[j]
    for k in team:
      score_team2 += data[member-1][k-1]
  result.append(abs(score_team2-score_team1))

print(min(result))