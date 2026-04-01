import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*[bisect_left(a, x) for x in b])