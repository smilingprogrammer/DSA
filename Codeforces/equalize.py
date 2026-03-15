import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(set(map(int, input().split())))
    
    ans, l = 1, 0
    for r in range(a):
        while a[r] - a[l] > n - 1:
            l += 1
        ans = max(ans, r - l + 1)
    
    print(ans)