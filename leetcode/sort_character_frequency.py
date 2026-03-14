class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return ''.join(char * freq for char, freq in sorted(c.items(), key=lambda x: -x[1]))