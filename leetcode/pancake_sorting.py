class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        
        def flip(end):
            start = 0
            while start < end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        
        N = len(A)
        output = []
        
        for i in range(N - 1, -1, -1):
            max_ = i
            for j in range(i, -1, -1):
                if A[j] > A[max_]:
                    max_ = j
            
            if max_ != i:
                flip(max_)
                flip(i)
                output.append(max_ + 1)
                output.append(i + 1)
        
        return output