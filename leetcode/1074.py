class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        def count_our_subarrays(nums, target):
            unique_target_count = defaultdict(int)
            unique_target_count[0] = 1
            
            our_count = 0
            one_d_psum = 0
            
            # Need to comeback to this later to check the range
            for i in nums:
                one_d_psum += i
                our_count += unique_target_count[one_d_psum - target]
                
                unique_target_count[one_d_psum] += 1
                
            return our_count
            
        r, c = len(matrix), len(matrix[0])
        output = 0
        
        # for i in matrix:
        #     output += i.count(target)
            
            
        # for 
        for head in range(r):
            c_sum = [0] * c
            
            for down in range(head, r):
                for col in range(c):
                    c_sum[col] += matrix[down][col]
            
                output += count_our_subarrays(c_sum, target)
        
        return output
        
        
        
        
        
        
        
        
        
        
        
# [1,-1].  i = 0
# [-1,1]

# j = 0

# [1  -1  1 -1]
# [-1  1  -1  1]
# [1  -1  1 -1]
# [-1  1  -1  1]


# 1  0.  1   0

# 0.  0.  0.  0

# 3 + 2  + 3 + 4 + 2 + 2 = 16


