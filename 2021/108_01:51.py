from math import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))

g = 0
for i in a:
    g = gcd(g, i)

if k % g == 0 and k <= max(a):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')