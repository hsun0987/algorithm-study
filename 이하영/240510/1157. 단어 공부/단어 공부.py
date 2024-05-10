w = input().upper()
w_list = list(set(w)) #문자열 내에 중복 문자 제거 해서 리스트로 변환

cnt = []

for i in w_list:
  cnt.append(w.count(i))

if cnt.count(max(cnt)) > 1:
  print("?")
else:
  print(w_list[cnt.index(max(cnt))]) #w_list안에서 cnt의 최대값과 동일한 위치에 있는 값 출력