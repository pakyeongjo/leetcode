class ValidParentheses:
    def solution(self, s):
        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False

        stack = []
        hashmap = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif char in hashmap.keys():
                if not stack or hashmap[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
