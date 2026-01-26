t = int(input())

for i in range(t):
    a,b,c = map(int, input().split())

    # while i < 5
    # for i in range(5):
        if a<=b and a <= c:
            a = a + 1

        elif b <= a and b<=c:
            b = b +1

        else:
            c = c + 1

    i+=1

    solution = a * b * c
    print(solution)