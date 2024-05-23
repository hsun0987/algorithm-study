#pop을 해서 입력한 수열을 완성시키면 됨
#단, 스택에는 오름차순대로 한 번씩 push할 수 있음. 
#ex) 1, 2, 3, 4 push 후 4,3 pop 다시 5, 6 push 후 6 pop

# 1. 수열 입력 받기
# 2. 스택에 해당 수열의 값만큼 오름차 순대로 push, op에 + 저장
# 3. 스택의 맨 위 값이 해당 수열의 값과 같으면 pop, op에 - 저장
# 3-1. 같지 않다면 no 출력

import sys

n = int(sys.stdin.readline())
stack = [] 
op = [] # +, - 저장
count = 0
possible = True

for _ in range(n):
  num = int(sys.stdin.readline())

  while num > count:
    count += 1
    stack.append(count)
    op.append('+')

  if stack[-1] == num:
    stack.pop()
    op.append('-')
  else:
    possible = False
    break

if possible:
  for i in op:
    print(i)
else:
  print("NO")