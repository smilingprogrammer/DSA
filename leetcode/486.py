class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(i, j):
            if i == j:
                return nums[i]
            
            pick_left = nums[i] - solve(i + 1, j)
            pick_right = nums[j] - solve(i, j - 1)

            return max(pick_left, pick_right)

        return solve(0, len(nums) - 1) >= 0
        
        # player1 = 0
        # player2 = 0
        # nums.sort()

        # n = len(nums)
        # last = len(nums) - 1
        # i = 0

        # while i < len(nums):

        #     if i == last:
        #         player1 += nums[i]
        #         break

        #     num_two = nums[i:i+2]

        #     if i % 2 == 0:
        #         player1 += num_two[-1]
            
        #     else:
        #         player2 += nums[-1]

            # print(player1)
            # print(player2)
            # player1 += max(nums[i], nums[i+1])
            # i += 2


        # for i in range(1, len(nums)):

        #     next2
        #     if i % 2 == 0:
        #         player2 ()

        # print(nums)