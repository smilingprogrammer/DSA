t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    den = n * n - 1

    y_num = n * a[0] - a[-1]

    if y_num < 0 or y_num % den != 0:
        print("NO")
        continue

    y = y_num // den
    x = a[0] - y * n

    if x < 0:
        print("NO")
        continue

    ok = True

    for i in range(1, n + 1):
        expected = x * i + y * (n - i + 1)
        if a[i - 1] != expected:
            ok = False

            break

    print("YES" if ok else "NO")