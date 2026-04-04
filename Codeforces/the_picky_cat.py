import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    x = abs(a[0])
    smaller = 0

    for i in range(1, n):
        if abs(a[i]) < x:
            smaller += 1

    if smaller <= n//2:
        print("YES")

    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()