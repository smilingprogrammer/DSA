t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    possible = False
    for p in range(n):
        valid = True
        for i in range(n):

            if a[i] <= 2 * abs(i-p):
                valid = False
                break
        
        if valid:
            possible = True
            break

    if possible:
        print("YES")
    else:
        print("NO")