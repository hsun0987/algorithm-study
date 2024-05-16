n = int(input())
group = []

for _ in range(n):
  age, name = map(str, input().split())
  group.append((int(age), name))

group.sort(key = lambda x:x[0]) #나이를 기준으로 정렬, 나이가 같으면 들어온 순으로 정렬을 해야 하지만, 이미 들어온 순서대로 정렬이 되어 있으므로 나이만 고려

for i in group:
  print(i[0], i[1])