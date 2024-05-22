#문제 이해가 드럽게 안됐다. 
#m = 찾고자 하는 문서의 현재 위치(원래 큐) 
#출력값 = 우선순위가 적용된 큐에서의 m 문서의 위치
from collections import deque

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  priority = deque(list(map(int, input().split())))

  count = 1 #출력될 수 있는 가장 작은 숫자
  while True:
    if priority[0] == max(priority): #첫번째의 문서가 제일 중요한 문서일 경우
      if m == 0:
        print(count) #그게 m 문서라면 count 출력
        break
      else:  
        priority.popleft()  #아니라면 출력함
        count += 1 #출력 했으므로 증가
    
    else:   #첫번째 문서가 제일 중요한 문서가 아닐 경우
      priority.append(priority.popleft()) #한 칸씩 앞으로 땡김

    m -= 1 #m의 순서도 땡김
    if (m < 0): #그런데 m이 제일 앞이었다면 
      m = len(priority) - 1 #맨 뒤로 이동