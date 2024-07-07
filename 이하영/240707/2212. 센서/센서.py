# 센서 위치 조절? 가능 -> 오름차순으로 정렬
# 집중국 K개 만큼 집단을 나누려면 k-1개로 끊어줘야 함


import sys
input = sys.stdin.readline

N = int(input()) # 센서의 개수
K = int(input()) # 집중국의 개수
sensor = list(map(int, input().split()))
sensor.sort()

distance = [] #센서 간 거리

for i in range(N-1):
    distance.append(sensor[i+1]-sensor[i])
    
distance.sort(reverse=True)

print(sum(distance[K-1:]))