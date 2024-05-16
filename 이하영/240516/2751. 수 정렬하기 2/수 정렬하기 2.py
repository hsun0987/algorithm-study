#1차 시도 때 input()으로 입력 받음 -> 시간 초과
import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
  num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
  print(i)