m, n = map(int, input().split())

for i in range(m, n+1):
  if i == 1:
    continue
  for j in range(2, int(i**0.5) + 1): #m과 n의 약수 존재는 n의 제곱근까지 만 나누어 떨어지는 수가 있는지 확인해보면 됨 
    if i % j == 0: #나누어 떨어지는 수가 있는지 확인
      break
  else:
    print(i)