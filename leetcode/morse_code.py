class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
        ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
        ".--","-..-","-.--","--.."]

        seen = set()

        for word in words:
            morse_word = ""

            for c in word:
                index = "abcdefghijklmnopqrstuvwxyz".index(c)
                morse_word += morse_code[index]

            seen.add(morse_word)

        return len(seen)