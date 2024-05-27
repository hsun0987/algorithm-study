# 스택
# 1. 탑의 맨 왼쪽은 무조건 0, 레이저가 닿지 않는 탑의 결과도 0이므로 결과를 담는 리스트를 0으로 초기화
# 2. 레이저는 오른쪽에서 왼쪽으로 쏘니까 뒤에서부터 반복문 실행 
# 3. 스택에 현재 탑의 인덱스 push
# 4. 현재 탑이 스택에 담긴 탑보다 높으면 쓸모를 다 했으니 pop (현재 탑의 오른쪽에 있는 탑과 비교 = 레이저를 쏜 탑의 왼쪽에 있는 탑이 현재 탑)

import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))

result = [0] * n
stack = []

for i in range(n-1, -1, -1):
    while stack and (top[i] > top[stack[-1]]):
            result[stack[-1]] = i + 1 
            stack.pop()
    stack.append(i)

for i in result:
    print(i, end=' ')
        
