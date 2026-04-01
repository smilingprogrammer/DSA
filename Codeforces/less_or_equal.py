import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = sorted(map(int, input().split()))

if k == 0:

    if a[0] > 1:
        print(1)
    else:
        print(-1)
else:
    x = a[k - 1]

    if x < 1:
        print(-1)
    elif k < n and a[k] == x:
        print(-1)
    else:
        print(x)