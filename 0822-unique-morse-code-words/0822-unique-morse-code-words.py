class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_set = set()

        for word in words:
            morse_word = ""

            for c in word:
                morse_word += morse[ord(c) - ord('a')]

            morse_set.add(morse_word)

        return len(morse_set)
        