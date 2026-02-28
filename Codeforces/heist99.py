from collections import Counter

t = int(input())
for _ in range(t):
    num_alch = int(input())
    array_elements = list(map(int, input().split()))
    
    # maximum = max(array_elements)
    c = Counter(array_elements)

    # if array_elements.count(maximum) % 2 == 1:
    if all(v%2 == 0 for v in c.values()):
        print("NO")
    else:
        print("YES")