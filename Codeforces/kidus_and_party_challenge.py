t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odds = 0
    for x in a:
        if x % 2 != 0:
            odds += 1
    evens = n - odds

    print(min(odds, evens))