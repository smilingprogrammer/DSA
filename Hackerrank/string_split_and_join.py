
def split_and_join(line):
    # write your code here
    word_array = line.split()
    return "-".join(word_array)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)