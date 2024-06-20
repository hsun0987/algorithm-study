# 동전의 최소 개수 
# 2 * x + 5 * y 
# y부터 계산하고 나머진 x로
# for 문 - > 시간초과

import sys
input = sys.stdin.readline


n = int(input())

result = 0
while n > 0:
    if n == 1: # 처음부터 1이거나, 연산 후 1만 남을 경우
        result = -1
        break
    
    if n % 5 == 0:
        result += n // 5
        break
    else:
        n -= 2
        result += 1
        
        
print(result)