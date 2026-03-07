import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort(reverse=True)
    b.sort()
    
    total = sum(a)
    savings = 0
    ptr = 0
    
    for coupon in b:
        if ptr + coupon <= n:
            savings += a[ptr + coupon - 1]
            ptr += coupon
        else:
            break
    
    print(total - savings)