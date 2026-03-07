t = input()
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# my_list = n + m

# for i in range(len(my_list)):
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    

# # print(n)
# print(*my_list)


merged = []
first, second = 0, 0
while first < len(list1) and second < len(list2):
    if list1[first] < list2[second]:
        merged.append (list1[first])
        first += 1
    else:
        merged.append (list2 [second])
        second += 1
merged.extend(list1[first:])
merged.extend(list2[second:])

print(*merged)