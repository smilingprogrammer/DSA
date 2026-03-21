n, m = map(int, input().split())

lo, hi = 1, n

for _ in range(m):
    clue = input().split()

    i = int(clue[-1])
    if clue[2] == "left":
        hi = min(hi, i - 1)
    else:
        lo = max(lo, i + 1)

if lo > hi:
    print(-1)
else:
    print(hi - lo + 1)