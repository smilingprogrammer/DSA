n, k = map(int, input().split())

counts = (n + 1) // 2

if k <= counts:
    k_dev = 2 * k
    print(k_dev - 1)
else:
    k_dev = k - counts
    print(2 * k_dev)