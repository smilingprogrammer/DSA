n = int(input())
nums = list(map(int, input().split()))

odds = [x for x in nums if x % 2 != 0]
evens = [x for x in nums if x % 2 == 0]

if odds and evens:
    print(*sorted(nums))
else:
    print(*nums)