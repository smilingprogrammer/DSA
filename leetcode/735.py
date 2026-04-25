class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for i in asteroids:
            destroyed = False
            while stack:
                if i < 0 and stack[-1] > 0:
                    if abs(i) > stack[-1]:
                        stack.pop()
                        continue
                    elif abs(i) == stack[-1]:
                        stack.pop()
                        destroyed = True
                        break
                    else:
                        destroyed = True
                        break
                else:
                    break
            else:
                stack.append(i)
                continue

            # if i > 0 or (i < 0 and (not stack or stack[-1] < 0)):
            if not destroyed:
                stack.append(i)
            # if stack and i + stack[-1] >= 0:
            #     stack.append(i)

            # else:
            #     stack.pop()

        # print(stack)
        return stack