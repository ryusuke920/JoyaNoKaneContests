from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
c.sort()

ans = 0
for i in range(n):
    s = bisect_left(a, b[i])
    t = n - bisect_right(c, b[i])
    ans += max(0, t * s)

print(ans)