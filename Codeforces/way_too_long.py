num = int(input())

# my_input = "localization"
for i in range(num):
    my_input = input()
    if len(my_input) > 10:
        length_input = len(my_input) - 2
        first = my_input[0]
        last = my_input[-1]
        print(f"{first}{length_input}{last}")
    else:
        print(my_input)
