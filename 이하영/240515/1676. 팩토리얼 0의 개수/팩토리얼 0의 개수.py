n = int(input())

# 끝자리에 0이 나오려면 10이나 5가 들어가야 됨 -> 10에도 5가 들어가니 5가 몇 번 들어가는지 확인
count = 0
for i in range(1, n+1):
    if i % 5 == 0:
        count += 1
    if i % 25 == 0:
        count += 1
    if i % 125 == 0:
        count += 1
# 1차 시도 : 25, 125 등 5가 여러번 곱해진 경우는 생각 못 해서 틀림
print(count)