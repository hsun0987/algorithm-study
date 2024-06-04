# 중위 : 왼쪽 -> 루트 -> 오른쪽
# 중위 순회로 탐색된 노드 순서를 보고 트리의 모습을 출력해라 (오 -> 중-> 왼)
# 루트노드는 입력 받은 값들의 중앙 값 
# 중앙 값을 기준으로 왼쪽, 오른쪽 나눔
# (나눈 왼쪽에서의) 루트 노드 또한 중간에 있는 값 (재귀)
# 반복
# 입력 -> 본인을 key으로, 자식 노드(왼쪽 오른쪽) value
import sys

K = int(sys.stdin.readline()) #트리의 깊이

building = list(map(int, sys.stdin.readline().split()))
level = [[] for _ in range(K)]

def reverse_inorder(tree, depth):
    if len(tree) == 1:
        level[depth].append(tree[0])   #전달받은 배열의 길이가 1이면 서브트리에서 마지막 노드라는 뜻이므로 재귀를 더이상 하지 않고 종료
        return
    root = len(tree)//2 
    level[depth].append(tree[root])  
    
    reverse_inorder(tree[:root], depth+1) #루트(중앙값)을 기준으로 왼쪽에 있는 것들을, 다음 층수로 넘어가므로 +1해서 전달
    reverse_inorder(tree[root+1:], depth+1) #루트(중앙값)을 기준으로 오른쪽에 있는 것들을, 다음 층수로 넘어가므로 +1해서 전달
    
reverse_inorder(building, 0) #인덱스 0은 실질적으로 1층이므로
for i in range(K):
    print(*level[i], sep = ' ')