L = int(input())
string = input()
result = 0
for i in range(L):
    a = ord(string[i]) - 96
    result += a * (31**i)
print(result % 1234567891) 