class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        x, y = target

        dist = abs(x) + abs(y)

        for x_ghost, y_ghost in ghosts:
            dist_g = abs(x - x_ghost) + abs(y - y_ghost)
            if dist_g <= dist:
                return False

        return True