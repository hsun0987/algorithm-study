# 중복을 허용하지 않는 조합
# (의상 종류, 의상 이름)
# (옷종류 1의 갯수 + 1) X (옷 종류 2의 개수 + 1) X ... -1 
# +1을 하는 이유는 그 옷의 종류를 선택하지 않는 경우도 포함해야 하기 때문
# -1을 하는 이유는 옷 종류마다 선택하지 않는 경우가 선택될 경우는 제외해야 하기 때문 
import sys

T = int(sys.stdin.readline())
for _ in range(T) : 
    n = int(sys.stdin.readline())
    
    clothes = dict()
    for _ in range(n):
        name, kind = map(str, sys.stdin.readline().split())
        if kind not in clothes: #처음 등장하는 옷 종류라면
            clothes[kind] = [name]   #하나의 키에 여러 값을 추가하려면 값을 리스트로 변환 후 추가해야 함
        else: #등장 했던 옷 종류라면
            clothes[kind].append(name)
    
    result = 1
    
    for key in clothes.keys():
        result *= (len(clothes[key]) + 1)
        
    print(result - 1)