class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        
        def helper(index, combination):
            if index == len(digits):
                result.append(combination)
                return []
            
            for letter in digitDict[digits[index]]:
                helper(index + 1, combination + letter)
        
        if digits:
            helper(0, '')
        
        return result