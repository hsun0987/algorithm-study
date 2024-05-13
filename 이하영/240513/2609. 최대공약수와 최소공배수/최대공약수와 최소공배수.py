#유클리트 호제법 GCD(n, m) = GCD(m, r) (n mod m = r (0 <= r < m), n>= m)

n, m = map(int, input().split())
nn, mm = max(n, m), min(n, m)
while mm > 0:
  nn, mm = mm, nn % mm

gcd = nn
lcm = n * m // gcd
print(gcd)
print(lcm)