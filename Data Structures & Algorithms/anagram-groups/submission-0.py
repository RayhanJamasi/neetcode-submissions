class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        charList = {}
        finalList = []

        for word in strs:
            
            key = "".join(sorted(word))

            charList.setdefault(key, []).append(word)

        return list(charList.values())







        