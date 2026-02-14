t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    sum_a = sum(a)
    
    if sum_a % n != 0:
        print(-1)
    
    # k = 0
    # for candies in a:
    #     if candies > target:
    #         k += 1
    #         print(k)

    else:
        target = sum_a // n
        k = sum(1 for x in a if x > target)
        print(k)