t = int(input())
for _ in range(t):

    a, b, c = map(int, input().split())
    max_num = 0

    # if a >= b and a >= c:
    #     max_num = a
    # elif b >= a and b >= c:
    #     max_num = b

    # else:
    #     max_num = c

    # print(max_num)

    if a + b == c or  a + c == b or b + c == a:
        print("YES")
    else:
        print("NO")