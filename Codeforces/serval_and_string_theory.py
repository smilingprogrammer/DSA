t = int(input())
 
for _ in range(t):
    
    n, k = map(int, input().split())
 
    a = input().strip()
    
    universal = False
    if (k == 0 and a >= a[::-1]) or len(set(a)) == 1 :
        universal = False
    
    else:
        universal = True
            
    if universal:
        print('YES')
    else:
        print('NO')