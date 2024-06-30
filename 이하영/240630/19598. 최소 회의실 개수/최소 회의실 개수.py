# 진행되고 있는 회의들 중에서 빨리 끝나는 시간과 다음 진행될 회의의 시작 시간 비교

import sys
import heapq
input = sys.stdin.readline

N = int(input()) # 배열의 크기

mr = [] # 회의실
for _ in range(N):
    s, e = map(int, input().split()) # s = 회의 시작, e = 회의 끝
    mr.append([s, e])
    
mr.sort() # 빨리 시작하는 순으로 정렬

hq = [] # 회의 진행 정보

for start, end in mr:
    if hq and hq[0] <= start: # 회의가 진행되고 있는게 있다면, 진행하고 있는 회의의 끝나는 시간과 대기하고 있는 회의의 시작 시간 비교
       heapq.heappop(hq) # 다음 진행할 회의 시작 시간이 크거나 같으면 해당 회의실 비움(다음 진행할 회의를 위해)
    heapq.heappush(hq, end) # 현재 진행중인 회의의 끝나는 시간 업데이트 해줌
    
print(len(hq))
       