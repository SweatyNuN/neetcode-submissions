class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = Counter(list(s))
        t_list = Counter(list(t))
        if s_list == t_list:
            return True
        else:
            return False