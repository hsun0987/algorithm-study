# 1. ( 나오면 스택에 push
# 2. ) 나오면 (공통적으론 스택 pop )  ( ()는 레이저거나 막대의 처음과 끝을 알리는 것이므로 제외해야 하니까 )
# 2-1. 직전 괄호가 ) 라면 레이저가 나타났다는 뜻이므로 (수만큼 잘림, 스택에 (가 push 된 만큼 카운팅(스택의 길이)
# 2-2. )라면 마지막이라는 의미. +1 카운팅

laser = input()
stack = []
count = 0

for i in range (len(laser)):
    if laser[i] == "(":
        stack.append(laser[i])
    elif laser[i] == ")":
        stack.pop()
        if laser[i-1] == "(":
            count += len(stack)
        else:
            count += 1

print(count)