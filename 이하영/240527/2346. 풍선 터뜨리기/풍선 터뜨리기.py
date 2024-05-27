# 1. 덱에 종이에 적힌 수와 순서(인덱스 번호) 저장 -> enumerate 사용 (입렵된 순서, 입력값이 한 세트로 저장됨)
# 2. 터트린 후(pop)
# 3. 풍선에 적힌 숫자 만큼 rotate (rotate에 인자가 양수라면 반시계 방향으로 회전하므로 앞에 음수를 붙여줌)
# 3-1. 풍선에 적힌 수가 양수라면 풍선이 터진 자리도 포함시켜야 하는데 pop해서 없어짐 -> -1해줌
# 3-2. 음수라면 그대로 ㄱㅊ
import sys
from collections import deque

n = int(sys.stdin.readline())
num = deque(enumerate(map(int, sys.stdin.readline().split())))

while num:
    index, move = num.popleft() #처음 인덱스에 담긴 정보를 각각 index, move에 저장
    print(int(index)+1, end = ' ')
    
    if move > 0: #양수라면
        num.rotate( -(move - 1))
    elif move < 0: # 음수라면   
        num.rotate(-move)
        
        