# 두 파일을 합칠 때 필요한 비용 = 두 파일 크기의 합
# 작은 수부터 더해줘야 함
import sys, heapq
input = sys.stdin.readline

T = int(input()) # 테스트케이스

for _ in range(T): 
    K = int(input())  # 소설을 구성하는 장의 수
    page = list(map(int, input().split())) # 각 장의 파일 크기
    heapq.heapify(page) # 우선순위 큐로 바꿔줌
    
    result = 0  # 지금까지 발생한 비용
    
    while len(page) != 1: # 마지막 결과만 남을 때까지 
        a = heapq.heappop(page) # 첫번째 작은 값
        b = heapq.heappop(page) # 두번째 작은 값
        
        result += (a + b)
        
        heapq.heappush(page, a+b) # 합친 값 다시 넣어줌
        
    print(result)