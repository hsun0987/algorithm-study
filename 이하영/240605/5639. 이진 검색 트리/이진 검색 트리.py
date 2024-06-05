#전위 -> 원상태, 원상태 -> 후위 순회
# 전위순회에서 첫번째 값(루트)보다 커지는 숫자부터 오른쪽 서브트리 (50 / 30 24 5 28 / 45 98 52 60)
# 배열의 첫번째 값을 기준으로
# 루트보다 작은 것(왼쪽), 큰 것 나눔(오른쪽)
# 나눈 작은 것에서도 작은 것 큰 것 나눔 (반복)
# 루트보다 큰 숫자가 없을 때 -> 

import sys
sys.setrecursionlimit(10 ** 6)

def postorder(start, end):
    if start > end: # 순서가 역전됐다면 다 돌았다는 뜻이므로 종료
        return
    else:
        root = tree[start]
        division = end+1 #왼쪽 서브트리만 있을 경우 오른쪽 서브트리 방문을 끊기 위해 end보다 +1 해줌, 아래 반복문 속 조건문도 진행 x
        for i in range(start+1, end+1): #처음은 root이므로, start+1부터 end까지 비교 
            if root < tree[i]: #루트보다 더 큰 숫자가 나오면
                division = i #나누는 기준이 됨
                break
        postorder(start+1, division-1)
        postorder(division, end)
        print(root) #왼쪽 -> 오른쪽 -> 루트 순으로 출력문 실행됨
        
        
tree = []

for _ in range(10000):
    try:
        node = int(sys.stdin.readline())
        tree.append(node)
    except:
        break

postorder(0, len(tree)-1 ) #처음과 끝 인덱스 번호 넘겨줌
    

    
