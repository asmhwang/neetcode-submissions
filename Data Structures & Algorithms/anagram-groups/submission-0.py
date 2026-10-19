class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        temp = []
        for i in range(len(strs)):
            temp.append("".join(sorted(strs[i])))
        for i in range(len(strs)):
            if hm.get(temp[i]) is None:
                hm[temp[i]] = [strs[i]]
            else:
                hm[temp[i]].append(strs[i])
        ans = []
        for value in hm.values():
            ans.append(value)

        return ans
