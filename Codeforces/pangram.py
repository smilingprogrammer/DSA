n = int(input())
string_input = str(input())
alphabet = set('abcdefghijklmnopqrstuvwxyz')

if alphabet.issubset(set(string_input.lower())):
    print("YES")
else:
    print("NO")