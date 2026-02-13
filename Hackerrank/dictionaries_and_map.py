# Enter your code here. Read input from STDIN. Print output to STDOUT
# def main(the_num, my_input):
n = int(input())

new_dict = {}
for i in range(n):
    my_input = input().split()
    new_dict[my_input[0]] = my_input[1]

try:
    while True:
        new_input = input()
        if new_input in new_dict:
            print(f"{new_input}={new_dict[new_input]}")
        else:
            print("Not found")
except EOFError:
    pass
