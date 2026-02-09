class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        word=""
        for char in s:
            if char!=" ":
                word+=char
            elif word:
                words.append(word)
                word=""
        if word:
            words.append(word)
        words.reverse()
        return " ".join(words)
