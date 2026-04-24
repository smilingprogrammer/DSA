class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        for row in range(len(matrix)):
            # print(matrix[row][0])
            if target == matrix[row][0]:
                return True

            if target > matrix[row][0]:
                left, right = 0, len(matrix[row]) - 1
                while left <= right:
                    middle = (left + right) // 2

                    if matrix[row][middle] == target:
                        return True
                    if matrix[row][middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1

        return False