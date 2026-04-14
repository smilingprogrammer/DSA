n = int(input())
a = list(map(int, input().split()))

a.sort()

day = 1

for x in a:
    if x >= day:
        day += 1

print(day - 1)