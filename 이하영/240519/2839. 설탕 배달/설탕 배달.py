# (3 * x) + (5 * y)   -> x+y의 최소값
import sys

n = int(sys.stdin.readline())

count = 0

while n >= 0:
    if n % 5 == 0:    # 설탕의 무게가 5의 배수인 경우
        count += (n // 5)
        print(count)
        break
    else :
        n -= 3
        count += 1  # 3키로 무게의 가방이 하나 추가됨
else:
    print(-1) # n이 0보다 작을 때 -1 출력