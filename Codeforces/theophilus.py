import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if 'A' not in s or 'B' not in s:
        print(0)
        continue
    
    first_a = s.index('A')
    last_b = len(s) - 1 - s[::-1].index('B')
    
    print(max(0, last_b - first_a))