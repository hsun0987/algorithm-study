T = int(input())

for i in range(T) :
   h, w, n = map(int, input().split())
   y = n % h
   x = n // h + 1
   if y == 0:
      x = n // h
      y = h
   print(y*100 + x)