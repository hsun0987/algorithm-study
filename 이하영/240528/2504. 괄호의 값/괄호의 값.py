# 1. 괄호 리스트로 받아옴
# 2. 반복문을 돌리다가
# 3. (,[ 가 나오면 stack에 push, 괄호에 맞는 값을 변수에 곱해줌
# 4. ), ] 가 나오면 
# 4-1. 직전에 들어있는 괄호가 짝이 맞는 괄호 인지 확인 후 맞으면 덧셈 연산 
# 4-2. 짝이 안맞으면 0 출력 후 종료
# 4-3. 스택 pop 후(괄호의 짝을 찾았으니까), 해당 값에 맞는 나누기 연산(열린 만큼 곱해준 변수를 다음 연산을 위해 1로 만들어주는 작업)


import sys

brackets = sys.stdin.readline()
stack = []
answer = 1 #곱하기만 한 값을 저장
result = 0 #더하기까지 한 결과를 저장

for i in range (len(brackets)):
    if brackets[i] == "(" :
        stack.append(brackets[i])
        answer *= 2
    elif brackets[i] == "[" :
        stack.append(brackets[i])
        answer *= 3
    elif brackets[i] == ")":
        if brackets[i-1] == "(":
            result += answer
        elif not stack or stack[-1] != "(":
            result = 0
            break
        stack.pop()
        answer //= 2
    elif brackets[i] == "]":
        if brackets[i-1] == "[":
            result += answer
        elif not stack or stack[-1] != "[":
            result = 0
            break
        stack.pop()
        answer //= 3

if stack:
    print(0) #짝이 맞지 않아서 남은 경우
else:
    print(result)