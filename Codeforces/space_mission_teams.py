n, d = map(int, input().split())

p = list(map(int, input().split()))

p.sort()

output = 0

left, right = 0, n-1

while left <= right:
    i = p[right]

    what_need = d // i + 1

    if right - left + 1 >= what_need:
        output += 1
        left += what_need - 1
        right -= 1
    else:
        break

print(output)

# for i in p:
#     count += 1
#     if count * i > d:
#         output += 1
#         count = 0

# print(output)