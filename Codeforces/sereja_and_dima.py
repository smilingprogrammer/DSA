n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
sereja = 0
dima = 0

for turn in range(n):
    if cards[left] > cards[right]:
        if turn % 2 == 0:
            sereja += cards[left]
        else:
            dima += cards[left]
        left += 1

    else:
        if turn % 2 == 0:
            sereja += cards[right]
        else:
            dima += cards[right]

        right -= 1

print(sereja, dima)