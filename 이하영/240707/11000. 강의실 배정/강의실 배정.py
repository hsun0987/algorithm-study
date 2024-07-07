import sys
import heapq
input = sys.stdin.readline

N = int(input()) # 수업의 수

mr = [] # 강의실
for _ in range(N):
    s, e = map(int, input().split()) # s = 수업 시작, e = 수업 끝
    mr.append([s, e])
    
mr.sort(key = lambda x: x[0]) # 빨리 시작하는 순으로 정렬

hq = [] # 수업 진행 정보

for start, end in mr:
    if hq and hq[0] <= start: 
       heapq.heappop(hq) 
    heapq.heappush(hq, end) 
    
print(len(hq))
       