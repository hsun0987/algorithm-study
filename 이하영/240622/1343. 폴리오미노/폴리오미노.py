# 14916 거스름돈 문제와 비슷
# 길이가 더 긴 AAAA 먼저 처리 후 남은 문자 중 xx가 있으면 xx를 BB로 처리

import sys
input = sys.stdin.readline


board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)
        
