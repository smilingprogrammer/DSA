password = input().strip()
number_of_trials = int(input().strip())
trials = [input().strip() for _ in range(number_of_trials)]


if password in trials:
    print("YES")
else:
    has_front = False
    has_back = False
    for trial in trials:
        if trial[1] == password[0]:
            has_front = True

        if trial[0] == password[1]:
            has_back = True

    if has_front and has_back:
        print("YES")

    else:
        print("NO")