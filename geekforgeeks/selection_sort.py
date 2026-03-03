class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(0, len(arr) - 1):
            minimum_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minimum_idx]:
                    minimum_idx = j
                    
            arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i]
            
        return arr