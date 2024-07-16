import sys

N = int(input()) # 도시의 개수 

dp = [0] * (N+1)


def fibo(n):
    if n == 1 or n == 2:
        return 1
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(N))