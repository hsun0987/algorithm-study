# 각 레벨의 너비 = 맨 오른쪽 노드 열 번호 - 맨 왼쪽 노드 열 번호 + 1
# 레벨은 1(루트노드)부터 1씩 증가하며 내려감
# 구하는 것 : 너비가 가장 넓은 레벨, 그 레벨의 너비 ( 단, 정답이 될 레벨이 2개 이상이라면 가장 작은 값의 레벨을 답으로)
# 노드의 위치 => 구하려는 노드의 왼쪽에 위치하는 노드의 개수 + 1 -> 중위 순회로 
# 트리 노드 -> 부모 노드가 없는 노드
# 트리 깊이 -> DFS
# 노드 저장 tree[i][0] = 왼, tree[i][1] = 오
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input()) # 노드의 개수
tree = [[-1, -1] for _ in range(N+1)] # -1은 노드가 들어있지 않다는 뜻
tree_parent = [-1] * (N+1)

column = 1
node_info = dict() # key : 노드 깊이, value : 노드 번호, 노드 열

def depth_and_col (v, depth): #노드 번호, 깊이
    global column #열은 겹치지 않기 때문에
    
    if v == -1: # 노드가 들어있지 않으면 리턴
        return
    
    depth_and_col(tree[v][0], depth+1) #왼쪽
    
    if depth not in node_info: # 새로운 층이라면
        node_info[depth] = [] 
    node_info[depth].append((v, column)) # 루트
    column += 1
    
    depth_and_col(tree[v][1], depth+1) # 오른쪽
    
        
for _ in range(N):
    me, l, r = map(int, input().split())
    tree[me][0] = l
    tree[me][1] = r
    
    if l != -1 :
        tree_parent[l] = me
    if r != -1 :
        tree_parent[r] = me

for i in range(1, N+1):
    if tree_parent[i] == -1 and(tree[i]): #부모 노드는 없고, 자식 노드는 있을 때
        root = i
        break

depth_and_col(root, 1)

max_width = 0
max_level = 0

for level in sorted(node_info.keys()):
    cols = [info[1] for info in node_info[level]] # info[0] = 노드 번호, info[1] = 레벨
    
    width = max(cols) - min(cols) + 1# 해당 레벨에서 가장 큰 열 - 가장 작은 열
    if width > max_width: # 저장된 너비보다 이번 레벨의 너비가 더 크다면
        max_width = width
        max_level = level
        
print(max_level, max_width)