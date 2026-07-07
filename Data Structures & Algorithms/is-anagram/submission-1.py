class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = Counter(s)
        t_list = Counter(t)
        if s_list == t_list:
            return True
        else:
            return False