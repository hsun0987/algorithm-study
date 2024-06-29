# 인접한 원생들의 키 차이를 구해줌
# 키 차이가 많이 나는 구역을 기준으로 나눠줌
# 나눠지는 조는 k개, 나눠지는 선은 k-1개

import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n = 원생의 수, k = 조의 개수
child = list(map(int, input().split()))

kichai = []
for i in range(1, n):
    kichai.append(child[i] - child[i-1])

kichai.sort(reverse=True)

res = 0
for i in range(k-1, len(kichai)):    #키 차이가 많이 나는 구간 k-1곳을 제외하고 모두 더해줌
    res += kichai[i]
    
print(res)