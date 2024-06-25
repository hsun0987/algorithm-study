#  시작 시간 - 끝나는시간 - 시작 시간 - 끝나는 시간 .. 꼬리잡기
# 회의가 짧을 수록 여러 회의가 가능 -> 끝나는 시간으로 정렬
# 회의가 끝난 시간과 그 다음 회의의 시작 시간은 가까워야함 -> 시작 시간 정렬

import sys
input = sys.stdin.readline

N = int(input()) # 회의의 수

mr = [] # 회의실

for _ in range(N): 
    a, b = map(int, input().split()) # a = 회의 시작, b = 회의 끝
    mr.append([a, b])
    
mr.sort(key = lambda x: x[0]) # 빨리 시작하는 순으로 정렬
mr.sort(key = lambda x: x[1]) # 빨리 끝나는 순으로 정렬

end = mr[0][1] # 첫번째 회의가 끝나는 시간
count = 1

for i in range(1, N): # s = 시작시간, e = 끝나는 시간
    if mr[i][0] >= end: # 이번 회의 시작 시간이 이전 회의 끝난 시간과 같거나 그 후라면
        count += 1
        end = mr[i][1]
        
print(count)