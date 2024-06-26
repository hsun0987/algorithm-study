# - 가 나오면 괄호계산하는게 최솟값이 나옴 -> -를 기준으로 구분해서 마지막에 - 연산 처리

import sys
input = sys.stdin.readline

sic = input().strip() # 식 입력

part = sic.split('-') # - 기준으로 나눠줌

result = sum(map(int, part[0].split('+'))) # + 기준으로 문자열 자르고 + 연산
# result = 0으로 초기화하고, for문에서 첫번째 파트부터 연산을 하는 건 값이 다르게 나옴 ( result = result - part라 result에 첫번째 파트 값에서 음수가 씌어져 나옴)
for p in part[1:]: # 
    result -= sum(map(int, p.split('+')))
    
print(result)