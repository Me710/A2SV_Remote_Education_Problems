class Solution(object):
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            lowercase_word = word.lower()

            if set(lowercase_word).issubset(row1) or set(lowercase_word).issubset(row2) or set(lowercase_word).issubset(row3):
                result.append(word)

        return result
