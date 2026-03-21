from collections import defaultdict


k = int(input())
s = input()

freq = defaultdict(int)

freq[0] = 1
ones = 0
ans = 0

for c in s:
    if c == '1':
        ones += 1

    if ones >= k:
        ans += freq[ones - k]

    freq[ones] += 1

print(ans)