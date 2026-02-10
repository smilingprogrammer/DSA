t = int(input())

for _ in range(t):
    n, m, p, q = map(int, input().split())
    
    k = n // p
    r = n % p
    
    if r == 0:
        if m == k * q:
            print("YES")
        else:
            print("NO")
    else:
        
        print("YES")