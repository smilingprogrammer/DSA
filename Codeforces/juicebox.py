import sys
from collections import defaultdict

input = iter(sys.stdin.read().split()).__next__

def solve():
    n, k = map(int, input().split())
    brand_totals = defaultdict(int)
    for _ in range(k):
        b, c = map(int, input().split())
        brand_totals[b] += c
    
    totals = sorted(brand_totals.values(), reverse=True)
    print(sum(totals[:n]))

t = int(input())
for _ in range(t):
    solve()