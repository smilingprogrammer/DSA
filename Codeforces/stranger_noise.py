t = int(input())

for _ in range(t):
    len_s = int(input())
    s = str(input()).lower()

    new_s = s[0]

    for ch in s[1:]:
        if ch != new_s[-1]:
            new_s += ch


    if new_s == "meow":
        print("YES")

    else:
        print("NO")