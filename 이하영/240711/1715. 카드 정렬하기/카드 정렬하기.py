# 작은 수부터 더해줘야 함
import sys, heapq
input = sys.stdin.readline

N = int(input()) # 묶음 수

set = []
for _ in range(N): 
    s = int(input())
    heapq.heappush(set, s)
    
result = 0
while len(set) != 1: # set에 남은 묶음이 1개가 될 때까지
    
    a = heapq.heappop(set) # 첫번째로 작은 수
    b = heapq.heappop(set) # 두 번째로 작은 수
    
    result += (a + b)
    
    heapq.heappush(set, a + b)
    
print(result)