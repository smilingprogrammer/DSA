import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    vals = list(map(int, input().split()))
    
    a = [0, 0] + vals
    
    def rec(node, depth):
        if depth == n:
            return 0, 0
        
        left, right = 2 * node, 2 * node + 1
        ls, la = rec(left, depth + 1)
        rs, ra = rec(right, depth + 1)
        
        left_total = a[left] + ls
        right_total = a[right] + rs
        target = max(left_total, right_total)
        extra = (target - left_total) + (target - right_total)
        
        return target, la + ra + extra
    
    _, total_added = rec(1, 0)
    print(total_added)

solve()