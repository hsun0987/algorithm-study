N = int(input())
count = 1 #지나가는 벌집 개수
room = 1 # 몇 번째 방

while N > count:
    count += 6*room
    room += 1
 
print(room)
 #6, 12, 18, 24 6개씩 늘어나네