def swap_case(s):
    # output = ""
    # for ch in s:
    #     if ch.islower:
    #         output += ch.upper()
    #     else:
    #         output += ch.lower()
        # else:
        #     output += ch
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)