T = int(input())

for i in range(T):
  r, s = map(str, input().split())
  r = int(r)

  for j in s:
    print(j*r, end="") #end="" 로 줄바꿈 막음
  print()