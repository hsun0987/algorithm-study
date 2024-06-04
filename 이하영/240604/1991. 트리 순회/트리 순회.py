# 전위 : 루트 -> 왼쪽 -> 오른쪽
# 중위 : 왼쪽 -> 루트 -> 오른쪽
# 후위 : 왼쪽 -> 오른쪽 -> 루트

# 입력 -> 본인을 key으로, 자식 노드(왼쪽 오른쪽) value
import sys

N = int(sys.stdin.readline())

tree = dict()

for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]
    
def preorder(node): #전위
    print(node, end='') #루트부터 방문
    if tree[node][0] != ".":
        preorder(tree[node][0]) #왼쪽 탐색
    if tree[node][1] != ".":
        preorder(tree[node][1]) #오른쪽 탐색

def inorder(node): #중위
    if tree[node][0] != ".":
        inorder(tree[node][0]) #왼쪽 탐색
    print(node, end="")
    if tree[node][1] != ".":
        inorder(tree[node][1]) #오른쪽 탐색        
        
def postorder(node): #후위
    if tree[node][0] != ".":
        postorder(tree[node][0]) #왼쪽 탐색
    if tree[node][1] != ".":
        postorder(tree[node][1]) #오른쪽 탐색   
    print(node, end="")
    
preorder("A")
print()
inorder("A")
print()
postorder("A")