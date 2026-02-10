def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        # Separate odd and even, sort descending
        odd = sorted([x for x in a if x % 2 == 1], reverse=True)
        even = sorted([x for x in a if x % 2 == 0], reverse=True)
        
        # Compute prefix sums
        odd_prefix = [0]
        for x in odd:
            odd_prefix.append(odd_prefix[-1] + x)
        
        even_prefix = [0]
        for x in even:
            even_prefix.append(even_prefix[-1] + x)
        
        results = []
        for k in range(1, n + 1):
            max_score = 0
            
            # Try different combinations of odd and even coins
            for num_odd in range(min(k, len(odd)) + 1):
                num_even = k - num_odd
                if num_even > len(even):
                    continue
                
                # Sum must be odd to survive (odd count of odd numbers)
                if num_odd % 2 == 1:
                    score = odd_prefix[num_odd] + even_prefix[num_even]
                    max_score = max(max_score, score)
            
            results.append(max_score)
        
        print(' '.join(map(str, results)))

solve()