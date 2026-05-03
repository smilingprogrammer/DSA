import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    current_max = -1
    
    for x in a:
        if x >= current_max:
            count += 1
            current_max = x
    
    print(count)

