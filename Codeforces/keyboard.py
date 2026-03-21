t = int(input())
for _ in range(t):
    s = input()

    working = set()
    i = 0
    while i < len(s):
        j = i

        while j < len(s) and s[j] == s[i]:
            j += 1

        run_len = j - i

        if run_len % 2 == 1:
            working.add(s[i])

        i = j

    print(''.join(sorted(working)))