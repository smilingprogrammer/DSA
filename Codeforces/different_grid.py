import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    flat = []
    for i in range(n):
        flat += list(map(int, input().split()))
    
    nm = n * m
    if nm == 1:
        print(-1)
        continue
    
    # Cyclic shift by nm//2 to maximize "distance" (shift by 1 also works)
    k = nm // 2
    b = flat[k:] + flat[:k]
    
    # Verify (safety check)
    valid = all(b[i] != flat[i] for i in range(nm))
    if not valid:
        # Try shift by 1
        b = flat[1:] + flat[:1]
        valid = all(b[i] != flat[i] for i in range(nm))
    
    if not valid:
        print(-1)
    else:
        idx = 0
        rows = []
        for i in range(n):
            rows.append(' '.join(map(str, b[idx:idx+m])))
            idx += m
        print('\n'.join(rows))
