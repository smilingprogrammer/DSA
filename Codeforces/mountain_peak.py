t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    right_min = [0] * n
    right_min[n-1] = n-1

    for x in range(n - 2, -1, -1):
        if h[x] < h[right_min[x+1]]:
            right_min[x] = x

        else:
            right_min[x] = right_min[x+1]

    found = False
    left_min_idx = 0

    for j in range(1, n - 1):
        if h[left_min_idx] < h[j] and h[right_min[j+1]] < h[j]:
            print("YES")
            print(left_min_idx+1, j+1, right_min[j+1]+1)

            found = True

            break

        if h[j] < h[left_min_idx]:
            left_min_idx = j

            
        # i = -1
        # for x in range(j):
        #     if h[x] < h[j]:
        #         i = x
        #         break

        # k = -1
        # for x in range(j + 1, n):
        #     if h[x] < h[j]:
        #         k = x
        #         break

        # if i != -1 and k != -1:
        #     print("YES")
        #     print(i + 1, j + 1, k + 1)
        #     found = True
        #     break

    if not found:
        print("NO")