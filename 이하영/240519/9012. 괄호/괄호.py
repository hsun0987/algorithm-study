T = int(input())

for _ in range(T):
    
    stack = []
    str = input()
    for i in str:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':  # stack이 비워있지 않거나 이 전에 '('일 경우
                stack.pop()  # 스택에서 지워줌
            else:
                stack.append(i)  #그게 아니라면 stack에 추가하고 종료
                break
    
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
    