# n! / k!(n-k)! 구현
def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i-1)

n, k = map(int, input().split())

print(factorial(n) // (factorial(k) * factorial(n-k)))