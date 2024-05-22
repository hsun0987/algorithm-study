import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = []

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(n_list)/n))

#중앙값
n_list.sort()
print(n_list[n//2])

#최빈값
max_nl = Counter(n_list).most_common()
if len(max_nl) > 1:
  if max_nl[0][1] == max_nl[1][1]:
    print(max_nl[1][0])
  else:
    print(max_nl[0][0])
else:
  print(max_nl[0][0])

#범
print(max(n_list) - min(n_list))