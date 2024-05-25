#1. 테스트 케이스 개수 만큼 반복문 진행
#2. '-' 입력 -> pop
#2-1. '<' 입력 -> '<' 직전에 있는 문자를 어딘가에 보관 했다가 왼쪽으로 이동
#2-2. '>' 입력 -> '>' 직후에 있는 문자를 어딘가에 보관 했다가 오른쪽으로 이동
#2-3. 일반 문자 입력 -> 냅둠
# + 명령어로 인해 보관되는 문자들을 담을 보관소는 후입선출 = 스택
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    password = sys.stdin.readline().rstrip()
    move_pwd = [] #커서에 의해 이동 당할 문자들을 담음
    result_pwd = [] #최종적으로 완성될 비밀번호 담음 (password에서 하나하나 담음)
    
    for command in password:
        if command == '-':
            if result_pwd: #지울 패스워드가 존재할 경우에만 실행
                result_pwd.pop() #'-' 직전에 있는 문자 지움
        elif command == '<':
            if result_pwd: #문자가 없으면 이동할 필요가 없으니 존재 확인
                move_pwd.append(result_pwd.pop()) # <의 왼쪽으로 이동해야 하므로 직전에 있는 비번 일단 삭제 후 보관
        elif command == '>':
            if move_pwd: # '<' 명령어로 인해 보관된 문자가 있을 때만 실행(왼쪽 이동 없이 오른쪽으로만 이동하는건 아무 일이 일어나지 않음)
                result_pwd.append(move_pwd.pop()) #커서가 왼쪽으로 이동하느라 보관된 문자를 result_pwd로 옮겨줌
        else:
            result_pwd.append(command)
    
    print("".join(result_pwd) + "".join(reversed(move_pwd)))   #커서를 왼쪽으로 이동하면서 저장된 비번들이 move_pwd에 아직 남아있을 수도 있으니 문자열 합침
    # move_pwd는 스택이고, 스택은 후입선출이다. 특성상 반대로 쌓이므로 역순으로 다시 정렬해줌