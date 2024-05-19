while True:
    str = input()
    stack = []
    
    if str == '.':
        break
    
    for i in str:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':  # stack이 비워있지 않거나 이 전에 '['일 경우
                stack.pop()  # 스택에서 지워줌
            else:
                stack.append(i)  #그게 아니라면 stack에 추가하고 종료
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':  # stack이 비워있지 않거나 이 전에 '('일 경우
                stack.pop()  # 스택에서 지워줌
            else:
                stack.append(i)  #그게 아니라면 stack에 추가하고 종료
                break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")