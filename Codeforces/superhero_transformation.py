s = str(input())
t = str(input())

vowel = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"

ans = "No"

# i = j = 0

# while i < len(s) and j < len(t):
#     if s[i] in vowel and t[j] in vowel:
#         ans = "Yes"

#     elif s[i] in consonant and t[j] in consonant:
#         ans = "Yes"

#     else:
#         ans = "No"

#     i += 1
#     j += 1

# print(ans)


if len(s) != len(t):
    print("No")
else:
    ans = "Yes"
    for i in range(len(s)):
        if (s[i] in vowels and t[i] in vowels) or (s[i] in consonants and t[i] in consonants):
            continue
        else:
            ans = "No"
            break
    print(ans)