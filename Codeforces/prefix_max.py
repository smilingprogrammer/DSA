t = int(input())
# n = int(input())

# list_m = list(map(int, input().split()))

for _ in range(t):
    
    n = int(input())
    list_m = list(map(int, input().split()))

    maximum = max(list_m)

    if list_m[0] != maximum:
        for i in range(len(list_m)):
            if list_m[i] == maximum:

                # print("the maximum is:", maximum)
                # print("listm[i] is", list_m[i])
                list_m[i], list_m[0] = list_m[0], list_m[i]
                # print("after swap", list_m)
                break

    output = 0
    for i in range(len(list_m)):
        output += max(list_m[:i+1])

        # print("output for each", output)

    
    print(output)


# print(t)
# print(n)
# print(list_m)