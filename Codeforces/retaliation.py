t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


# x = a[1] - yn
# y = (n * a[1]) - (a[n]) / (n^2 - 1)
    first = n * n - 1

    second = n * a[0] - a[-1]

    if second < 0 or second % first != 0:
        print("NO")
        continue

    second_op = second // first
    first_op = a[0] - second_op * n

    if first_op < 0:
        print("NO")
        continue

    ok = True

    for i in range(1, n + 1):
        expected = first_op * i + second_op * (n - i + 1)
        if a[i - 1] != expected:
            ok = False

            break

    print("YES" if ok else "NO")









# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]


# [21-1, 18-2, 15-3 12-4 9-5] -> 1(1st)
# [20-5, 16-4, 12-3, 8-2, 4-1] -> 1(2nd)
# [15-5, 12-4, 9-3, 6-2, 3-1] -> 2(2nd)
# [10-5, 8-4, 6-3, 4-2, 2-1] -> 3(2nd)
# [5-5, 4-4, 3-3, 2-2, 1-1] -> 4(2nd)
# [0, 0, 0, 0, 0]


# [0 0 0 0 0]

# x = number of times we perform the first operation
# y = number of times we perform the second operation

# x*i
# y*n-i+1
# a[i] = x * i + y * (n - i + 1)

# a[1] = x * 1 + y * (n - 1 + 1)
# a[1] = x + yn
# a[n] = x * n + y * (n - n + 1)
# a[n] = xn + y

# a[1] = x + yn
# a[n] = xn + y

# n * a[1] = n * x + yn*n
# n * a[1] = nx + yn^2 ==> 3
# a[n] = xn + y ==> 2

# (n * a[1]) - (a[n]) = y(n^2 - 1)
# y = (n * a[1]) - (a[n]) / y(n^2 - 1)

# a[1] = x + yn
# x = a[1] - yn
# y = (n * a[1]) - (a[n]) / (n^2 - 1)

# 21 -> 5 1 (1st) + 4 (2nd)
# 18 -> 5
# 15 -> 5
# 21 18 15 12 9
# y = ((5 * 21) - (9)) / (5^2 - 1)
# y = 105 - 9 / 25 - 1
# y = 96 / 24
# y = 4

# x = 21 - 4*5
# x = 21 - 20
# x = 1