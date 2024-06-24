# 첫번째 음료를 제외한 음료의 양은 절반
# 처음 음료는 양이 제일 많은 음료로, 그 다음부터는 상관 없음

import sys
input = sys.stdin.readline

N = int(input()) # 유제품의 수

drink = list(map(int, input().split()))

drink.sort(reverse=True)

total = 0
for i in range(len(drink)):
    if i == 0:
        total = drink[i]
    else:
        total += (drink[i] / 2)
        
print(total)