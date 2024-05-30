# heapq 모듈은 최소 힙만 지원 
# 힙 삽입 -> heapppush (추가할 힙, 추가할 원소)
# 힙 삭제 -> heapppop(삭제할 힙) (최소 순으로 삭제)

import sys
import heapq 

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
  x = int(sys.stdin.readline())
  
  if x == 0:
    if heap:
      print(heapq.heappop(heap)[1]) # 힙에서 최소값을 삭제하고 출력, 인덱스 0은 절대값을 씌운 x임
    else:
      print(0) 
  elif x != 0:
    if x > 0:
      heapq.heappush(heap, (x, x)) # 원래 값을 함께 튜플로 넣어줌
    elif x < 0:
      heapq.heappush(heap, (-x, x)) # x의 값이 음수일 때 절대값으로 바꾼 후 튜플로 넣어줌