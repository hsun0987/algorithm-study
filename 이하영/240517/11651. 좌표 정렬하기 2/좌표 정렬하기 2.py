n = int(input())
list = []
for _ in range(n):
  x, y = map(int, input().split())
  list.append((x,y))

list.sort()
list.sort(key=lambda y: y[1])

for x, y in list:
  print(x, y)