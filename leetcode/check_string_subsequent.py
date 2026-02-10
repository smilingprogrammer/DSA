class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = "".join(word1)
        second = "".join(word2)

        if first == second:
            return True
        else:
            return False