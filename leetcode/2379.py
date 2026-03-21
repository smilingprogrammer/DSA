class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        min_whites = whites

        for i in range(k, len(blocks)):
            
            whites += (blocks[i] == 'W')
            whites -= (blocks[i - k] == 'W')
            min_whites = min(min_whites, whites)

        return min_whites