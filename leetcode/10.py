class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(s, p):

            # base case
            if len(p) == 0:
                return len(s) == 0
          
            # the astrekis case
            if len(p) > 1 and p[1] == '*':

                # ignore , skip to the second pattern
                if match(s, p[2:]):
                    return True

                # get matching
                if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                    return match(s[1:], p)

                return False

            else:
                if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                    return match(s[1:], p[1:])
                
                return False

        
        return match(s, p)