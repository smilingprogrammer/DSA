t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    unique_count = len(set(a))
    result = 2 * unique_count - 1
    
    print(result)