class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for i in range(len(strs)):

            word = strs[i]
            key = "".join(sorted(word))
            result.setdefault(key, []).append(word)

        return list(result.values())

        