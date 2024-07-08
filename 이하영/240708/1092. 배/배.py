# 크레인과 박스를 무게 순으로 내림차순 정렬
# 다 차면 제외

import sys
input = sys.stdin.readline

N = int(input()) # 크레인의 수
crane_w = list(map(int, input().split())) # 크레인 무게 제한
M = int(input()) # 박스의 수
box_w = list(map(int, input().split())) # 박스 무게 제한

crane_w.sort(reverse=True)
box_w.sort(reverse=True)

time = 0

if crane_w[0] < box_w[0]:
    print(-1)
else:
    while box_w: #박스가 남아있을 때까지 
        for c in crane_w: # 크레인에
            for b in box_w: # 박스를 옮김
                if c >= b: # 크레인에 실을 수 있는 박스 무게라면
                    box_w.remove(b) # 박스 무게 리스트에서 해당 박스 지움 (옮김 처리)
                    break
        time += 1   # 모든 크레인 한 바퀴 돌면 다음 턴으로 넘어감
        
    print(time)