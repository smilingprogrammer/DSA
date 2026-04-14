import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()

    l, r = 0, n - 1
    removed = []

    for ch in s:
        if ch == 'L':
            removed.append(a[l])
            l += 1
        else:
            removed.append(a[r])
            r -= 1


    ans = [0] * n
    cur = 1 % m

    for i in range(n - 1, -1, -1):
        cur = (cur * removed[i]) % m
        ans[i] = cur

    print(*ans)