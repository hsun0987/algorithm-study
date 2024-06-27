# 10^n : m의 개수는 n+1
# 5 * 10^n : m의 개수는 n개

# k를 기준으로 나눠줌
# 최대값 -> k까지 하나의 숫자로 봄
# 최솟값 -> k 나오기 전까지만 하나의 숫자로 봄

import sys
input = sys.stdin.readline

mingyeom = input().strip()

min_mg = '' # 최소값
max_mg = '' # 최대값

m = 0

for mg in mingyeom:
    if mg == 'M':
        m += 1
    elif mg == 'K':
        if m > 0: #앞에 m이 존재하면
            min_mg += str(10**(m-1)) 
            min_mg += str(5)
            max_mg += str(5 * (10**m))  
        else: # m이 존재하지 않으면
            min_mg += str(5)
            max_mg += str(5)
            
        m = 0
        
if m > 0: #끝이 K로 끝나지 않아 m이 남아있는 경우 고려
    min_mg += str(10**(m-1))
    for i in range(m):
        max_mg += str(1)
        
print(max_mg)
print(min_mg)