class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        if len(word1)==len(word2):
            for i in range(len(word1)):
                s =s+word1[i]+word2[i]
            return s
        elif len(word1)<len(word2):
            for i in range(len(word1)):
                s=s+word1[i]+word2[i]
            return s+word2[len(word1):]
        else:
            for i in range(len(word2)):
                s=s+word1[i]+word2[i]
            return s+word1[len(word2):]
        