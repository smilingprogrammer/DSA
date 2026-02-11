class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")


        for word in words:
            w = word.lower()
            if all(ch in first_row for ch in w):
                output.append(word)
            elif all(ch in second_row for ch in w):
                output.append(word)
            elif all(ch in third_row for ch in w):
                output.append(word)
            # else:
            #     return

        return output