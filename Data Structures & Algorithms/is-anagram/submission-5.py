class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dic = {}
        t_dic = {}
        
        for char in s:
            s_dic[char] = s_dic.get(char, 0) + 1

        for char in t:
            t_dic[char] = t_dic.get(char, 0) + 1

        if len(s_dic) == len(t_dic):
            for char in s:
                if s_dic[char] == t_dic.get(char, 0):
                    continue
                else:
                    return False

            return True

        else:
            return False
