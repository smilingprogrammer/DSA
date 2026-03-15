from collections import Counter

n = int(input())
my_input = input()

frequency = Counter(my_input)

if len(frequency) >= 2 and max(frequency.values()) == 1:
    print("No")
else:
    print("Yes")