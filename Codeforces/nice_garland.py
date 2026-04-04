# import sys

# input = sys.stdin.readline

# n = int(input())
# s = input()

# patterns = ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR"]

# best_prob = n + 1
# best_string = ""

# for p in patterns:
#     candidate = []
#     changes = 0

#     for i in range(n):
#         ch = p[i % 3]
#         candidate.append(ch)
#         if s[i] != ch:
#             changes += 1

#         if changes < best_prob:
#             best_prob = changes
#             best_string = "".join(candidate)

# print(best_prob)
# print(best_string)


n = int(input())
s = input()

patterns = ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR"]

best_changes = n + 1
best_string = ""

for p in patterns:
    changes = sum(1 for i in range(n) if s[i] != p[i % 3])
    if changes < best_changes:
        best_changes = changes
        best_string = "".join(p[i % 3] for i in range(n))

print(best_changes)
print(best_string)