import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    bad = []

    for k in range(n // 2):
        if s[k] != s[n - 1 - k]:
            bad.append(k)

    if not bad:
        print("Yes")
    elif bad[-1] - bad[0] == len(bad) - 1:
        print("Yes")
    else:
        print("No")