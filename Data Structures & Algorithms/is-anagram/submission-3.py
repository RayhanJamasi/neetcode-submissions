class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for char in t:
            dic[char] = dic.get(char, 0) - 1

        return all(number == 0 for number in dic.values())