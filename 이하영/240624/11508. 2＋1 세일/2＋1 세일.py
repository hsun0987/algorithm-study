# 유제품 3개 사면 가장 싼 제품은 무료
# 최소비용 -> 가격이 높은 순대로 정렬 후 3개 씩 묶어서 삼

import sys
input = sys.stdin.readline

N = int(input()) # 유제품의 수

diary = []
for _ in range(N):
   diary.append(int(input()))
   
diary.sort(reverse=True) 

total = 0
for i in range(N):
    if (i+1) % 3 != 0: # 3배수일 경우 무료, 배열의 인덱스는 0부터 시작하므로 i에 1을 더해줌
        total += diary[i]
        
print(total)