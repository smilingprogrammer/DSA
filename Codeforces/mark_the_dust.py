t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    total = 0

    seen_positive = False

    for i in range(n - 1):
        if a[i] > 0:
            seen_positive = True
            total += a[i]

        elif seen_positive:
            total += 1

    print(total)