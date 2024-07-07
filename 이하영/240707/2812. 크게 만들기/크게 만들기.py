# 스택에 있는 숫자와 현재 숫자 비교
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N = 자리 수, K = 지울 숫자 개수
num = list(input()) # N자리 수

result = [] # 결과를 담을 스택
delk = K
for n in num:
    while result and (result[-1] < n) and delk > 0:
        result.pop()
        delk -= 1
    result.append(n)
    
print(''.join(result[:N-K]))