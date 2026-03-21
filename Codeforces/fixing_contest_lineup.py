t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for k in range(n+1):
        if all(a[j] <= b[k + j] for j in range(n - k)):
            print(k)
            break