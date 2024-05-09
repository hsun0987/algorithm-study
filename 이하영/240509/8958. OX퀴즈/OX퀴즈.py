num = int(input())

for i in range(num):
  case = input()
  count = 0
  total = 0
  for j in case:
    if j == 'O':
      count += 1
      total += count
    else:
      count = 0
  print(total)