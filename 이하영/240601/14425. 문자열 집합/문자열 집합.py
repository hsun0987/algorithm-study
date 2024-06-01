import sys

n, m = map(int, sys.stdin.readline().split())

s = set(sys.stdin.readline().rstrip() for _ in range(n))   #중복을 허용하지 않으므로 set(집합)

count = 0 # 일치하는 문자열의 개수

for _ in range(m):
    str = sys.stdin.readline().rstrip()   #검사해야할 문자열
    
    if str in s: #str가 집합 S에 있으면
        count += 1 
print(count)