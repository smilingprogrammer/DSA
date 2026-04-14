t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    cntB = s.count('B')

    if cntB == k:
        print(0)
        continue

    print(1)

    if cntB < k:
        need = k - cntB
        cntA = 0
        for i in range(n):
            if s[i] == 'A':
                cntA += 1
            if cntA == need:
                print(i + 1, 'B')
                break
    else:
        need = cntB - k
        cntB_seen = 0
        for i in range(n):
            if s[i] == 'B':
                cntB_seen += 1
            if cntB_seen == need:
                print(i + 1, 'A')
                break