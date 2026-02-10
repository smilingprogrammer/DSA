#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        # a = set(a)
        # b = set(b)
        # if all(item in b for item in a):
        #     return True
            
        # else:
        #     return False
        # return all(item in b for item in a)
        c1 = Counter(a)
        c2 = Counter(b)
        
        is_subset = all(c2[item] <= c1[item] for item in c2)
        if is_subset:
            return True
        else:
            return False
    