#후위표기법 -> 후위 표시 후 가장 앞 연산자부터 계산
# 스택 -> 연산자를 담음 (스택인 이유 : 후입선출이라)
# 연산자 순위 (), */, +- 
# 괄호 안에 있는 연산자가 출력 1순위, 곱셈나눗셈이 2순위, 합차는 3순위
# 1. (가 등장하면 스택에 push
# 2. )가 나오면 스택에 담겨있던 것들 pop
# 3. * 또는 / 가 나오면 스택에 */ 있는지 확인
# 3-1. 있으면 담겨 있는 */ 중 최상단에 있던 것만 pop 후 스택에 push
# 4. + - 는 스택에 (가 있는지 확인
# 4-1. (가 있으면 스택에 담긴 것들 pop 후 +, -을 스택에 push 
# 5. A, B 등의 문자는 결과를 저장하는 리스트에 push
# 6. 결과를 담은 리스트는 문자열로 바꾼 후 출력

jung = input()

stack = [] #후위 표기식 스택
hu = ''

for i in jung:
    if i.isalpha():
        hu += i
    elif i == "(":
        stack.append(i)
    elif i ==")":
        while stack and stack[-1] != "(" : # 스택의 top이 (가 될 때까지
            hu += stack.pop()
        stack.pop() # ( 필요 없어져서 제거
    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] == '/' ):
            hu += stack.pop()
        stack.append(i)
    elif i == "+" or i == "-":
        while stack and stack[-1] != '(':
            hu += stack.pop()
        stack.append(i)
   
while stack:
    hu += stack.pop()
    
print(hu)
        
        
