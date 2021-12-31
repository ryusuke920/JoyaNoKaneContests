s = input()
ans = 0
white = 0
for i, j in enumerate(s):
    if j == 'W':
        ans += i - white
        white += 1

print(ans)