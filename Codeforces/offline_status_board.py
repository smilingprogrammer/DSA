import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i, x in enumerate(a):
        pos[x] = i
    
    suffix_len = 1
    for i in range(n - 2, -1, -1):
        if pos[b[i]] < pos[b[i + 1]]:
            suffix_len += 1
        else:
            break
    
    print(n - suffix_len)