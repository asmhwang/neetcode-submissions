class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current=""
        ans=""
        for i in strs[0]:
            current+=i
            length=len(current)
            for j in range(len(strs)):
                if strs[j][:length]!=current:
                    return ans
            ans= current
        return ans