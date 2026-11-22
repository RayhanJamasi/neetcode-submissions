class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        max_len = 0
        curr_len = 0
        seen = set()

        while right < len(s):

            if s[right] in seen:
                seen.remove(s[left])
                left += 1

            else:
                seen.add(s[right])
                curr_len = len(seen)
                
                if (curr_len > max_len):
                    max_len = curr_len
                right += 1

        return max_len
            


            