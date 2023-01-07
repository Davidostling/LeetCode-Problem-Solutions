class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        outputList = []
        digitString = ""
        for element in digits:
            digitString += str(element)
        digitInt = int(digitString) + 1
        for element in str(digitInt):
            outputList.append(int(element))
        return outputList

#Problem description: https://leetcode.com/problems/plus-one/description/