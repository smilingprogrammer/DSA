def squareit(x):
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid*mid <= x:
            left = mid + 1

        else:
            right = mid - 1

    return right


n, k = map(int, input().split())

dureti = 9 + 8 * (n + k)

p = (-3 + squareit(dureti)) // 2
e = n - p

print(e)