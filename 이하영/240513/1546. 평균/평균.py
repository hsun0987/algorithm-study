N = int(input())
real = list(map(float, input().split()))
fake = []
max_score = max(real)

for i in range(N):
  fake.append(real[i] / max_score * 100)

print(sum(fake) / N)