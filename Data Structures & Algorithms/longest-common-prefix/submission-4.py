class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        shortest_len = min(len(s) for s in strs)

        for i in range(0, shortest_len):
            chars = set()
            for word in strs:
                chars.add(word[i])
            if len(chars) == 1:
                result += chars.pop()
            else:
                return result
        return result