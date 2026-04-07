class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack=[]
        for i  in range(len(logs)):
            if stack and logs[i]=="../":
                stack.pop()
            elif logs[i]== "./":
                continue
            elif logs[i]!="../":
                stack.append(logs[i])
                
        return len(stack)