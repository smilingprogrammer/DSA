class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # a = 'a'
        # b = 'b'
        # if a < b:
        #     print(1)
        # else:
        #     print(2)
        left, right = 0, len(letters)-1
        first = 0

        while left <= right:
            middle = (left + right) // 2

            if letters[middle] > target:
                first = middle
                right = middle - 1
            else:
                left = middle + 1

        if first == 0:
            return letters[0]
        else:
            return letters[first]