# 총 인구 수의 절반이 되는 인구수의 마을이 우체국 위치

import sys
input = sys.stdin.readline

N = int(input()) # 마을의 수

village = []
people = 0
for _ in range(N):
    x, a = map(int, input().split()) # 마을의 위치, 마을에 살고 있는 사람의 수
    village.append([x, a])
    people += a # 총 인구 수
    
village.sort(key = lambda x : x[0]) # 마을 위치 순서대로 정렬

p = 0 # 순회하며 센 마을 인구 누적 수
 
for x, a in village:
    p += a
    
    if p >= (people / 2): # 현재 마을까지의 인구 합이 전체 인구의 절반보다 같거나 많다면
        print(x) # 그 마을이 우체국 위치
        break
    