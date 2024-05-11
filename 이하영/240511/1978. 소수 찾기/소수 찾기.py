N = int(input())
n_list = list(map(int, input().split()))

count = 0

for i in n_list:
    false = 0
    if i == 1:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                false = 1
        if false == 0:
            count += 1
        
print(count)