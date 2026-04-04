n = int(input())
a = list(map(int, input().split()))

start_ones = 0
for x in a:
    if x == 1:
        start_ones += 1
    else:
        break

end_ones = 0
for i in range(n - 1, -1, -1):
    if a[i] == 1:
        end_ones += 1

    else:
        break

max_ones = 0
current = 0

for x in a:
    if x == 1:

        current += 1
        max_ones = max(max_ones, current)

    else:
        current = 0

result = max(max_ones, end_ones + start_ones)

print(result)