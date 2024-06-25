# 근손실 최소 합 -> 앞 뒤의 합 비교
# 홀수일 경우  -> 근손실 가장 큰 기구 먼저 설정

import sys
input = sys.stdin.readline

N = int(input()) # 운동기구 갯수
t = list(map(int, input().split()))

t.sort()

if N % 2 == 1: # 홀수일 경우
    M = t.pop()
else:
    M = 0
    
for i in range(N//2):
    if t[i] + t[-(i+1)] > M: # 가장 큰 손실량과 가장 적은 손실량의 합이 M보다 작으면
        M = t[i] + t[-(i+1)]
        
print(M)