class Solution:
    def isValid(self, s: str) -> bool:
        letterDict = []
        for letter in s:
            if letter in "([{":
                letterDict.append(letter)
            elif letter in ")]}":
                if not letterDict:
                    return False
                if letter == ")" and letterDict[-1] != "(":
                    return False
                if letter == "]" and letterDict[-1] != "[":
                    return False
                if letter == "}" and letterDict[-1] != "{":
                    return False
                letterDict.pop()

#Problem description: https://leetcode.com/problems/valid-parentheses/description/