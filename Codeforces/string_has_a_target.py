t = int(input())

# print(s[::-1])
for _ in range(t):

    len_s = input()
    s = input().strip()
    min_char = min(s)

    i = s.rfind(min_char)
    # print(i)
    result = s[i] + s[:i] + s[i+1:]

    print(result)
    # list_s = list(s[::-1])
    # for i in range(len(list_s)):

    #     if list_s[i] == "a":
    #         list_s.pop(i)
    #         list_s.insert(0, "a")
    #         break


    # print(list_s)
