a, b, c, d = map(int, input().split())

if a + b == c + d:
    print("Balanced")
elif a + b < c + d:
    print('Right')
else:
    print('Left')