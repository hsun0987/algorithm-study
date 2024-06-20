# 로프에 걸리는 무게 = 물체의무게 / 로프의 개수
# 물체의 무게 = 로프에 걸리는 무게 * 로프의 개수
# 만약 루프 하나가 들 수 있는 최대 무게가 1이라면, 1 * 루프개수가 물체의 최대 무개
# 루프의 무개가 1, 5, 6라면, 5, 6만 골라서 사용할 수 있음 (그럼 최대 무게 10)

import sys
input = sys.stdin.readline

N = int(input())  # 줄의 개수

rope_weight = []
for _  in range(N):
    rope_weight.append(int(input()))  # 로프가 버틸 수 있는 최대 중량
rope_weight.sort() # 루프의 무게가 작을수록 루프를 많이 써야됨 -> 루프 무게 * 루프 개수 계산 위한 정렬
    
result = 0
for k in rope_weight:
    result = max(result, k * N)
    N -= 1
    
print(result)