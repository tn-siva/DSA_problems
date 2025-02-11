class Solution:
    # Contains Duplicate Integer
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = []
        for item in nums:
            if item in exists:
                return True
            exists.append(item)
        return False

        ## Alternate
        #uniq = len(set(nums))
        #if uniq < len(nums):
        #    return True
        #return False

    # Are 2 strings anagrams
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_count = {}
        t_char_count = {}

        for index in range(len(s)):
            if s[index] in s_char_count:
                s_char_count[s[index]] += 1
            else:
                s_char_count.update({s[index]:1})
            if t[index] in t_char_count:
                t_char_count[t[index]] += 1
            else:
                t_char_count.update({t[index]:1})

        if s_char_count == t_char_count:
            return True
        else:
            return False

