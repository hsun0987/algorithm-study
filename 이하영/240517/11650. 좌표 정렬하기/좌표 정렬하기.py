n = int(input())
list = []
for _ in range(n):
  x, y = map(int, input().split())
  list.append((x,y))

list.sort()

for x, y in list:
  print(x, y)

#첫 시도 틀림 -> x 좌표가 같지 않아도 y를 기준으로 정렬이 됨