# 1로 끝나면 마지막에 1을 붙인 것 -> 1을 떼줌 (10으로 나눴을 때 나머지가 1인지 확인)
# 2로 나눠 떨어지는지 확인
# 반복 
# 전부 해당 없으면 -1 출력
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
count = 1 # 처음 연산 고려

while a != b: #b를 a로 만들어줌
    
    if a > b: # 연산 후 b가 a보다 작아지는건 안됨
        count = -1
        break
    
    if b % 10 == 1: # 끝자리가 1인지 확인
        b //= 10 # 1 없애줌
        count += 1
    elif b % 2 == 0: # 2로 나눠 떨어지는지 확인
        b //= 2
        count += 1
    else:
        count = -1
        break
    
print(count)