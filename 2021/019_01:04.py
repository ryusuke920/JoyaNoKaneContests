s = input()
t = 0
for i in s:
    if i == 'C' and t == 0:
        t = 1
    elif i == 'F' and t == 1:
        t = 2

print('Yes') if t == 2 else print('No')