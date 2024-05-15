n = int(input())

word_list = []
for _ in range(n):
    word_list.append(input())

set_word = list(set(word_list)) # set함수로 중복 제거
set_word.sort()
set_word.sort(key = len) #기준을 세워서 정렬, 여기선 길이를 기준으로 정렬

for word in set_word:
    print(word)