import sys
input = sys.stdin.readline

N = int(input()) 

town = []
people = 0
for _ in range(N):
    x, a = map(int, input().split())
    town.append([x, a])
    people += a 
    
town.sort(key = lambda x : x[0]) 

p = 0 
 
for x, a in town:
    p += a
    
    if p >= (people / 2): 
        print(x)
        break
    