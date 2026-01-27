class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert_to_string = str(x)
        if convert_to_string == convert_to_string[::-1]:
            return True
        else:
            return False