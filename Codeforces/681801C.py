import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    s = input().strip()

    consecutive = 0
    for c in s:
        if c == '1':
            consecutive += 1
            if consecutive >= k:
                print("NO")
                return
        else:
            consecutive = 0

    print("YES")

    ones_count = s.count('1')
    ones_rank  = 1
    zeros_rank = ones_count + 1

    result = []
    for c in s:
        if c == '1':
            result.append(ones_rank)
            ones_rank += 1
        else:
            result.append(zeros_rank)
            zeros_rank += 1

    print(*result)


t = int(input())
for _ in range(t):
    solve()