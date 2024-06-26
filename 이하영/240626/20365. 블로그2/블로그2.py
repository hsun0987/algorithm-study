# 하나의 색으로(가장 많이 칠해야 하는 색) 전부 칠한 다음 칸에 맞는 색만 다시 칠함
# R, B 개수 카운팅 -> 가장 많은 수로 칠함 (색칠 1회 추가)
# 가장 많은 수가 나오지 않는 색의 갯수 만큼 칠함 ( 답은 1(전체 페인트) + @ )
import sys
input = sys.stdin.readline

N = int(input()) # 문제의 수
paint = input().strip()

pre = ''
RC = 0
BC = 0

for color in paint:
    if color == 'R':
        if pre != 'R': # 그 전 컬러가 빨간색이 아니었다면
            RC += 1
            pre = 'R' # 현재 컬러 저장
    elif color == 'B':
        if pre != 'B':
            BC += 1
            pre = 'B'
            
print(1 + min(BC, RC))