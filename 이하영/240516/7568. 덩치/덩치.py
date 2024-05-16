n = int(input())
group = []
for _ in range(n):
  x, y = map(int, input().split())
  group.append((x, y))

for i in group: 
  rank = 1
  for j in group: 
    if i[0] < j[0] and i[1] < j[1]: #전자는 몸무게 비교, 후자는 키 비교
      rank += 1
  print(rank, end=' ')