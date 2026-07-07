class Solution:
    def isValid(self, s: str) -> bool:
        if not s or not isinstance(s, str):
            return False
    
        valid_characters = set('(){}[]')

        if set(s) <= valid_characters is False:
            return False

        valid_dict = {'(': ')', '{': '}', '[': ']'}
        char_stack = []

        for char in s:
            if char in valid_dict.keys():
                char_stack.append(char)
            else:
                if len(char_stack) > 0:
                    if char != valid_dict.get(char_stack[-1]):
                        return False
                    else:
                        char_stack.pop()
                else:
                    return False
        if len(char_stack) > 0:
            return False
        return True