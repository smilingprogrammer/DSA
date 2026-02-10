n = int(input())
s = input().strip()

target = "ACTG"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pos = {letters[i]: i for i in range(26)}

min_ops = float('inf')

for i in range(n - 3):
    ops = 0
    for j in range(4):
        diff = abs(pos[s[i + j]] - pos[target[j]])
        ops += min(diff, 26 - diff)
    min_ops = min(min_ops, ops)

print(min_ops)