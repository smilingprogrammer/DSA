class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sort_pos = sorted(range(len(position)), key=lambda i: position[i])

        answer = pre = 0

        for i in sort_pos[::-1]:
            t = (target - position[i]) / speed[i]
            
            if t > pre:
                answer += 1
                pre = t

        return answer
        # pos_len = len(position)
        # if pos_len == 1:
        #     return 1
        # output = []

        # for i in range(pos_len):

        #     output.append(position[i] + speed[i])

        # # print(output)
        # output_set = set(output)

        # if target in output_set:
        #     return len(output_set)
        # elif sum(output) <= target:
        #     return len(output_set) - 1