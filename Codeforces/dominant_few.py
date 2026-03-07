import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]
    
    found = False
    k = 1
    while k + (k + 1) <= n:
        elite_sum = prefix[n] - prefix[n - k]
        crowd_sum = prefix[k + 1]
        if elite_sum > crowd_sum:
            found = True
            break
        k += 1
    print("YES" if found else "NO")