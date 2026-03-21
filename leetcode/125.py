class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = "".join(i for i in s if i.isalnum()).lower()

        # if not s.strip():
        #     return True

        if new_s == new_s[::-1]:
            return True
        else:
            return False