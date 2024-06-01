# heapq 모듈은 최소 힙만 지원 
# 힙 삽입 -> heapppush (추가할 힙, 추가할 원소)
# 힙 삭제 -> heapppop(삭제할 힙) (최소 순으로 삭제)

# 최댓값과 최솟값을 나눠서 저장 
# 최댓값이 삭제될 대 최솟값의 힙에서도 같이 삭제가 되어야 함..,.,

import sys
import heapq 

T = int(sys.stdin.readline())

for t in range(T):
    K = int(sys.stdin.readline())
  
    min_heap = [] 
    max_heap = []
    pop_result = [False] * K   # 삭제 됐는지 확인 하는 리스트 기본값 = 삭제X
    for k in range(K):
        command = list(map(str, sys.stdin.readline().split()))  # command[0] -> 동작, command[1] -> 삽입할 숫자

        op = command[0]
        num = int(command[1])
        
        if op == 'I':
            heapq.heappush(min_heap, (num, k))
            heapq.heappush(max_heap, (-num, k))

        elif op == "D":
            if num == -1:   # 최솟값 삭제
                while min_heap and pop_result[min_heap[0][1]]: # 힙에 숫자가 남아있고, 최솟값 힙의 맨 처음 값의 해당하는 pop_result의 인덱스가 True일 경우 (최댓값 힙에서 이미 제거된 값이라면)
                    heapq.heappop(min_heap)                      # 최솟값 힙에서도 지워서 싱크 맞춤
            
                if min_heap: #최솟값 힙이 비어있지 않으면 삭제 연산 진행 
                    pop_result[min_heap[0][1]] = True   # 해당 값이 삭제 됐다고 표시
                    heapq.heappop(min_heap)
            
            # 이번 턴에서 지울 값이 최댓값 힙에서 이미 지운 값이라면 최솟값에서도 지워주며 싱크를 맞춰주고 (while 문), 싱크가 맞으면 최솟값 힙에서 삭제 연산 진행 
            
            elif num == 1: # 최댓값 삭제
                while max_heap and pop_result[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    pop_result[max_heap[0][1]] = True
                    heapq.heappop(max_heap)  
                          
    # 마지막 턴이 끝난 후에도 싱크가 맞는지 확인
    while min_heap and pop_result[min_heap[0][1]]:  
        heapq.heappop(min_heap)
    while max_heap and pop_result[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if min_heap :
        min = heapq.heappop(min_heap)
        max = heapq.heappop(max_heap)

        print( -max[0], min[0]) # 최댓값 힙에 값을 push할 때 음수로 변환 후 저장했으므로 결과를 출력할 때 앞에 다시 음수 처리
                
    elif not min_heap :
        print("EMPTY")