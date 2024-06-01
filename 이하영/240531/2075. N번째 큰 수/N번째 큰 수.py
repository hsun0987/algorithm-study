# heapq 모듈은 최소 힙만 지원 
# 힙 삽입 -> heapppush (추가할 힙, 추가할 원소)
# 힙 삭제 -> heapppop(삭제할 힙) (최소 순으로 삭제)

# 무작정 모든 입력을 다 큐에 넣는건 메모리 초과로 인해 실패함
# 힙에 5개만 저장 -> 입력이 들어 올 때마다 갱신(큰 수  top 5)
import sys
import heapq 

n = int(sys.stdin.readline())
heap = [] * n

for i in range(n):
  x = list(map(int, sys.stdin.readline().split()))
  if i == 0:
    for num in x:
      heapq.heappush(heap, num)

  else:
    for num in x:
      if heap[0] < num:    # 현재 힙의 최솟값이 입력 받은 값보다 작다면 
        heapq.heappop(heap)  # 힙 최솟값을 방출
        heapq.heappush(heap, num) # 힙에 새로운 값을 추가하며 최솟값이 바꿈

print(heapq.heappop(heap))