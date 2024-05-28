import sys

p = int(sys.stdin.readline())
hu = sys.stdin.readline().rstrip()
num = []
stack = []
for _ in range(p):
  num.append(int(sys.stdin.readline()))

for i in hu:
  if i.isalpha():
    stack.append(num[ord(i) - ord("A")]) # i가 A라면 num의 0번째 인덱스가 stack에 들어감, i가 B라면 1번째 인덱스가
  else:
    b = stack.pop() #스택에 A, B가 들어있었다면 b에는 B가, a에는 A가 들어감 
    a = stack.pop()

    if i == "+":
      stack.append(a+b)
    elif i == "-":
      stack.append(a-b)
    elif i == "*":
      stack.append(a*b)
    elif i == "/":
      stack.append(a/b)

print("%.2f" %stack[-1] )