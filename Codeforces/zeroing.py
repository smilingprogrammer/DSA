n, k = map(int, input().split())

array_elements = list(map(int, input().split()))

array_elements.sort()

results = []
prev = 0

for i in array_elements:
    if i != prev:
        results.append(i - prev)
        prev = i

for i in range(k):
    print(results[i] if i < len(results) else 0)