data = []
for i in range(8):
    data.append(int(input()))

tmp = sorted(data, reverse=True)
point = sum(tmp[:5])
print(point)
result = []
for i in range(5):
    result.append(data.index(tmp[i])+1)
result.sort()
for i in range(5):
    result[i] = str(result[i])

print(' '.join(result))