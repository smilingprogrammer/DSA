import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    groups = []
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        groups.append(list(range(i, j)))
        i = j
    
    if any(len(g) == 1 for g in groups):
        print(-1)
        continue
    
    p = [0] * n
    for g in groups:
        for k in range(len(g)):
            p[g[k]] = g[(k + 1) % len(g)] + 1
    
    print(*p)