import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}

for i in range(1, n+1):
  poketmon = sys.stdin.readline().strip()
  dic[i] = poketmon  # {key = i, value = poketmon}
  dic[poketmon] = i # {key = poketmon, value = i}

for _ in range(m):
  quest = sys.stdin.readline().rstrip() 

  if quest.isdigit(): #isdigit()는 문자열이 숫자인지 판별하는 함수
    print(dic[int(quest)])
  elif quest.isalpha(): #문자면 숫자 출력
    print(dic[quest])
