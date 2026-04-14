n, m = map(int, input().split())
a = list(map(int, input().split()))

buses = 1
current_load = 0

for group in a:
    if current_load + group <= m:
        current_load += group
    else:
        buses += 1
        current_load = group

print(buses)