t = int(input())
for _ in range(t):
    num_alch = int(input())
    list_of_enlevel = list(map(int, input().split()))
    seq = int(input())

    if min(list_of_enlevel) <= seq <= max(list_of_enlevel):
        print("YES")
    else:
        print("NO")