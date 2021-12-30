from collections import defaultdict

d1 = defaultdict(int)
d2 = defaultdict(int)

for i in range(int(input())):
    d1[input()] += 1
for i in range(int(input())):
    d2[input()] += 1

ans = 0
for k, v in d1.items():
    ans = max(ans, v - d2[k])

print(ans)