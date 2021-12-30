from collections import defaultdict

x = input()
d = defaultdict(str)
for i, j in enumerate(x):
    d[j] = chr(97 + i)

ans = []
for _ in range(int(input())):
    s = input()
    t = []
    for i in s:
        t.append(d[i])
    ans.append([''.join(t), s])

ans.sort(key = lambda x: (x[0], x[1]))
for i in ans:
    print(*i[1], sep='')