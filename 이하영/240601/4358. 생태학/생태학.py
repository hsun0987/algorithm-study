# (key, value)로 저장 key : 나무 이름 , value : 등장 횟수
# 사전순으로 정렬

import sys
from collections import defaultdict  #정렬해주는 딕셔너리 (트리맵)

treemap = defaultdict(int)
count = 0 # 입력 갯수
while True:

    tree = sys.stdin.readline().rstrip()
    
    if tree == "":
        break
    
    treemap[tree] += 1 # 각 나무의 등장 횟수 
    count += 1

sort_treemap = list(treemap.keys())
sort_treemap.sort()

for tree in sort_treemap:
    print("%s %.4f" %(tree, treemap[tree]/count*100))