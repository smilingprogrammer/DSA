import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ok = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            ok = False
            break

    if ok:
        print(0)
        continue

    ops = [(1, n)]

    for i in range(1, n - 1):
        if (a[0] + a[i]) % 2 == 1:
            ops.append((1, i + 1))
        else:
            ops.append((i + 1, n))

    print(len(ops))
    for l, r in ops:
        print(l, r)