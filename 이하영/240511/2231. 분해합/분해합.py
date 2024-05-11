N = int(input())
result = 0
for i in range(1, N+1):
    i_str = str(i)
    saengseong = 0
    for j in i_str:
        saengseong += int(j)
    
    total = i + saengseong
    
    if N == total:
        result = i
        break
print(result)