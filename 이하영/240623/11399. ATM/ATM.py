N = int(input())
P_sort = sorted(list(map(int, input().split()[:N])))
tot = 0

for i in range (1,N+1) :
    tot += sum(P_sort[:i])
print(tot)