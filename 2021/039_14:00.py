n, q = map(int, input().split())
s = input()

cnt = [0] * n
ac = 0
for i in range(n - 1):
    cnt[i + 1] += cnt[i]
    if s[i: i + 2] == 'AC':
        cnt[i + 1] += 1

for _ in range(q):
    l, r = map(int, input().split())
    print(cnt[r - 1] - cnt[l - 1])