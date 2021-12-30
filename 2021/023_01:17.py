from itertools import permutations

s, k = input().split()
k = int(k)

word = set()
for i in permutations(s):
    word.add(''.join(i))

word = list(word)
word.sort()
print(word[k - 1])