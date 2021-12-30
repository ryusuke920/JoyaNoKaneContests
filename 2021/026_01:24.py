s = input()
ans = 0
num = 'ATGC'
cnt = 0
for i in s:
    if i in num:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)