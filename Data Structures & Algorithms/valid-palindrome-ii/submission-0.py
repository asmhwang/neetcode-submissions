class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            new = s[:i]+s[i+1:]
            left = 0
            right = len(new)-1
            signal = 0
            while left<right:
                if new[left]!=new[right]:
                    signal=1
                    break
                left+=1
                right-=1
            if signal == 0:
                return True
        return False