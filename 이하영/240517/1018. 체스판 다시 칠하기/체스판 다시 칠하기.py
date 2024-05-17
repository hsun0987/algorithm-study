n, m = map(int, input().split())
board = []
result = []
for _ in range(n):
    board.append(input())

for x in range(n-7):
  for y in range(m-7): #8*8크기 고정 후 탐색
    black_paint = 0 
    white_paint = 0 
    for i in range(x, x+8):
      for j in range(y, y+8):
        if(i+j) % 2 == 0:   #짝수끼리 색이 같음
          if board[i][j] != 'W': #첫 시작이 흰색이 아닐 때
            white_paint += 1
          if board[i][j] != 'B': #첫 시작이 검정이 아닐 때
            black_paint += 1
        else:               #홀수끼리 색이 같
          if board[i][j] != 'B': 
            white_paint += 1
          if board[i][j] != 'W':
            black_paint += 1 

    result.append(white_paint)
    result.append(black_paint)


print(min(result))