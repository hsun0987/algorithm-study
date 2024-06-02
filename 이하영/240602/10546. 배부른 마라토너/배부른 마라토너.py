# 동명이인이 있을 수 있음
#(참가자이름, 이름 등장 횟수)
#완주하면 등장 횟수 -1 해줌
import sys

N = int(sys.stdin.readline())
maraton_list = dict()

for _ in range(N):
    chamgaja = sys.stdin.readline().rstrip()
    if chamgaja not in maraton_list.keys():  #동명이인이 없을 때
        maraton_list[chamgaja] = 1
    else: # 동명이인이 있을 때\
        maraton_list[chamgaja] += 1
    
for _ in range(N-1):
    wanjuja = sys.stdin.readline().rstrip()
    
    if wanjuja in maraton_list.keys():
        maraton_list[wanjuja] -= 1    #동명이인이 없는 완주자라면 value는 0

for key, value in maraton_list.items():
    if value == 1 : #완주자는 n-1 명이므로 완주하지 못한 사람의 value 값은 무조건 1
        print(key)