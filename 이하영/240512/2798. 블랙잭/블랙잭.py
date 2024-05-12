N, M = map(int, input().split())
card = list(map(int, input().split()))

total_list = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
           total = card[i] + card[j] + card[k]
           if total <= M:
               total_list.append(total)

print(max(total_list)) 