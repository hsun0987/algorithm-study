from collections import deque

N, K = map(int, input().split())
que = deque(range(1, N+1))

print("<", end="")
for i in range(N):
    for j in range(K-1):
        que.append(que.popleft())
    print(que.popleft(), end="")
    if i != (N-1): print(", ", end="")
print(">")