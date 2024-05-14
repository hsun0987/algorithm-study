# 첫 시도 : 메모리 초과 -> append, sort 사용으로 인한 입력이 원인
#각 인덱스에 입력된 수를 세서 그만큼 출력..?
import sys

n = int(sys.stdin.readline())
list = [0] * 10001
for _ in range(n):
  list[int(sys.stdin.readline())] += 1 #카운트 세기
for i in range(10001):
  if list[i] != 0:
    for _ in range(list[i]):
      print(i)
