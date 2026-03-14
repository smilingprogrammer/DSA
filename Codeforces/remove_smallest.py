t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    ok = all(a[i+1] - a[i] <= 1 for i in range(n-1))
    print("YES" if ok else "NO")