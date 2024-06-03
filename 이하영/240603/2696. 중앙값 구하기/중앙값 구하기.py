import sys

T = int(sys.stdin.readline())
for _ in range(T) : 
    M = int(sys.stdin.readline())
    
    suyeol = list(map(int, sys.stdin.readline().split()))
    for m in range(M//10):
        suyeol += list(map(int, sys.stdin.readline().split()))
        
    sort_suyeol = []
    answer = []
    for i in range(1, len(suyeol)+1):
        if i%2 == 0: #짝수번째인 경우
            sort_suyeol.append(suyeol[i-1])
        elif i%2 == 1: #홀수번째인 경우
            sort_suyeol.append(suyeol[i-1])
            sort_suyeol.sort()
            answer.append(sort_suyeol[(i-1)//2])
    
    print(len(answer))
    for i in range(len(answer)):
        if i % 10 == 0 and i > 1: #10, 20,... 번째라면 공백 출력, 인덱스 0번째도 나머지가 0으로 나오므로 1 이상인 조건 추가
            print()
        print(answer[i], end=" ")
        
        if i == len(answer):  #마지막 인덱스면 다음 테스트를 위해 다음 줄로 넘어감
            print()