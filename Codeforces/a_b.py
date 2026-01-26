my_input = int(input())
for i in range(my_input):
    num = input()
    a, b = num.split('+')
    print(int(a) + int(b))
