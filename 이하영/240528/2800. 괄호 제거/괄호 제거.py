import sys
from itertools import combinations

#1. 괄호의 위치 쌍 저장 -> 스택에 저장
#1-1. (에 위치를 먼저 저장하고 있다가, )가 등장하면 )의 위치와 함께 스택에 저장
#2. 괄호 위치를 저장한 리스트를 활용해 조합으로 괄호 제거 -> 제거한 수식을 리스트에 저장
#2-1. 제거는 해당 괄호의 위치의 문자를 공백으로 만들어서 함 (pop을 이용하려 했으나 '('를 제거하면서 인덱스의 번호도 달라져서 ')'를 제거할 때 범위를 벗어나는 오류 발생)
#3. 중복된 수식이 있을 수도 있으니 중복 제거 -> set()

susick = list(sys.stdin.readline().strip())

half, couple = [], []
result = set()

for i in range(len(susick)):
  if susick[i] == "(":
    half.append(i) # ( 의 위치 저장
  elif susick[i] == ")":
    couple.append((half.pop(), i))   # 순서대로 (, ) 의 위치 저장

for i in range(1, len(couple)+1):
  for combi in combinations(couple, i):
    temp = list(susick)
    for j in combi:
      temp[j[0]] = ""
      temp[j[1]] = ""
    result.add("".join(temp))

for i in sorted(list(result)):
  print(i)