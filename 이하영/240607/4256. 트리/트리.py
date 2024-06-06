# 루트노드 : 전위의 첫번째 
# 맨 왼쪽 노드 : 중위의 첫번쩨
# 중위 순회에서 루트 노드의 왼쪽 숫자들은 왼쪽 서브트리, 오른쪽 숫자들은 오른쪽 서브트리
# 루트노드를 기준으로 중위 순회를 왼쪽, 오른쪽 서브트리 2개로 슬라이싱
# 전위순회에서 처음 등장하는 숫자가 서브트리의 루트노드

# 정리 
# 1. 전위 순회 첫번째 인덱스와 일치하는 값을 중위 순회에서 찾기
# 2. 루트 노드의 위치로 왼쪽 서브트리, 오른쪽 서브트리 나눔(반복)

import sys
sys.setrecursionlimit(10000)

def solvedPost(prRoIn, start, end):
    if start > end:
        return
    
    root = Pre[prRoIn]
    root_index = In.index(root)  # 루트 노드의 인덱스를 중위 순회 리스트에서 찾기
    solvedPost(prRoIn + 1, start, root_index - 1)  # 왼쪽 서브트리
    solvedPost(prRoIn + (root_index - start) + 1, root_index + 1, end)  # 오른쪽 서브트리
    print(root, end=" ")
    
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    Pre = list(map(int, sys.stdin.readline().split()))
    In = list(map(int, sys.stdin.readline().split()))
    
    solvedPost(0, 0, n-1)
        
    print()
    