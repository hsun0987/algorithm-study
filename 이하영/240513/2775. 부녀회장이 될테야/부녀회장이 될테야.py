t = int(input())

for _ in range(t):
  k = int(input()) #층
  n = int(input()) #호

  floor0 = [i for i in range(1, n+1)]
  
  for i in range(k):
    for j in range(1, n):
      floor0[j] += floor0[j-1]

  print(floor0[n-1])