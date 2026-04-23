from collections import defaultdict
n = int(input())

char = ['A', 'S', 'V']
# dict_char = {ch: i for i, ch in enumerate(char)}

# print(len(char))
if n == 1:
    print(4)
else:
    dictionary_sec = defaultdict(int)

    # Loop for all the 4 chars
    # for c in range(4):
    #     dictionary_sec[(c, -1)] = 1


    for x in char:
        for y in char:
            if x!=y:
                dictionary_sec[(x,y)] += 1

    # Since its 1 we start from 2
    for _ in range(3, n + 1):
        new_dictionary_sec = defaultdict(int)

        for (x, y), count in dictionary_sec.items():
            for z in char:
                if z == y:
                    continue
                if x == 'S' and y == 'V' and z == 'A':
                    continue
                # if pprev == dict_char['S'] and prev == dict_char['V'] and next == dict_char['A']:
                    # continue
                new_dictionary_sec[(y, z)] += count

        dictionary_sec = new_dictionary_sec

    print(sum(dictionary_sec.values()))