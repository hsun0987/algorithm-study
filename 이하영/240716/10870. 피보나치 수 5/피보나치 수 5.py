import sys
input = sys.stdin.readline

n = int(input())

if n == 0 : 
    result = 0
elif n == 1 : 
    result = 1
else :
    f1 = 0
    f2 = 1
    result = 0
    for i in range(2, n+1) :
        result = f1 + f2
        f1 = f2
        f2 = result
    
print(result)