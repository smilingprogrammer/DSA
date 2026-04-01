import sys
input = sys.stdin.readline

n, t = map(int, input().split())
a = list(map(int, input().split()))

best = 0
total = 0
l = 0

for r in range(n):
    total += a[r]
    while total > t:
        total -= a[l]
        l += 1
    best = max(best, r - l + 1)

print(best)