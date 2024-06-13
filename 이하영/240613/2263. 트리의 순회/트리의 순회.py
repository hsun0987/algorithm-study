# 전위순회를 해라 (루트 -> 왼 -> 오)
# 루트 노드 : 중위의 중간값, 후위의 마지막 값
# inOrder에서 루트노드의 위치를 찾기 위해 .index를 썼더니 시간 초과가 뜸
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def SolvedPre(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root = postO[post_end]
    root_index = inorder_index[root]
    
    print(root, end=" ")
    
    left_tree_size = root_index - in_start #오른쪽 서브트리 내에서 왼쪽 서브트리 구할 때를 고려해 in_start 만큼 빼주기
    SolvedPre(in_start, root_index-1, post_start, post_start + left_tree_size - 1)
    # ^ 중위 순회에서 왼쪽 서브트리, 후위 순회에서 왼쪽 서브트리 
    SolvedPre(root_index+1, in_end, post_start + left_tree_size, post_end-1)
    # ^ 중위 순회에서 오른쪽 서브트리, 후위 순회에서 오른쪽 서브트리

N = int(input()) # 노드의 개수

inO = list(map(int, input().split())) #중위
postO = list(map(int, input().split())) # 후위

inorder_index = [0 for _ in range(N+1)]

for i in range(N):    # 루트노드 인덱스를 구하기 위해 중위 순회로 담긴 노드들의 인덱스 저장 (노드 번호, 인덱스)
    inorder_index[inO[i]] = i
     
SolvedPre(0, N-1, 0, N-1)
