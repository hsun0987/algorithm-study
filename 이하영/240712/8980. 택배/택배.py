# 본부 -> 박스 출발지, 도착지, 보낼 박수 개수 알고잇음
# 트럭 무게제한 있음
# 한 방향 운행, 도착지 변경 불가능, 마을이 보내는 박스 10개 중 3개만 실어도 됨
# 트럭 한 대로 배송할 수 있는 최대 박스 수 구하기

# 도착지가 빠른 것부터 처리 해야됨
 
import sys, heapq
input = sys.stdin.readline

N, C = map(int, input().split()) # N = 마을 수, C = 트럭 용량

M = int(input()) # 보내는 박수 정보의 개수

delivery_info = []
for _ in range(M):
    departure, arrival, count = map(int, input().split()) # 출발지, 도착지, 박스 개수
    delivery_info.append([departure, arrival, count])

delivery_info.sort(key = lambda x : (x[1], x[0])) # 받는 마을 기준으로 오름차순

total = 0 # 트럭에 실린 박스 개수
truck = [0] * N # N번째 마을에 도착할 때까지 실려있는 박스의 수

for dep, arr, cnt in delivery_info:
    current = cnt # 현재 마을에서 실어야 할 박스 수
    
    # 트럭에 실을 때 현재까지 트럭에 실린 박스 수를 고려해서 박스를 실어야 함 
    for i in range(dep, arr): # 도착할 때까지 박스는 실려있음 (1번 째 마을에서 3번째 마을로 보내는 박스라면 2번째 마을에 도착 할때도 실려 있음)
        if current + truck[i] >= C: # 트럭에 실려있는 박스와 이번 마을에서 보내야할 박스의 합이 트럭 최대 용량을 초과한다면
            current = C - truck[i] # 남은 용량만큼만
        truck[i] += current        # 트럭에 실음
        
    total += current
    
    
print(total)
    