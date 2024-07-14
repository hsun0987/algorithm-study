import sys

city = int(input())
distance = list(map(int, sys.stdin.readline().split()[:city-1]))
cost = list(map(int, sys.stdin.readline().split()[:city]))
total = 0
lowest = cost[0]

for i in range(len(cost)-1) :
    if lowest > cost[i] :
        lowest = cost[i]
    total += (lowest*distance[i])

print(total)