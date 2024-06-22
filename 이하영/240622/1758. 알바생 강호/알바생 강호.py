# 팁이 큰 순대로 줄 세움

import sys
input = sys.stdin.readline

n = int(input())

tip = []
for _ in range(n):
    tip.append(int(input()))
    
tip.sort(reverse=True)

res = 0

for i in range(n):
    t = tip[i] - i    # i는 0부터 시작하므로 -1 해주지 않아도 됨
    
    if t > 0: # 양수인 경우만
        res += t
    
print(res)