class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sList = list(s)
        tList = list(t)
        sDict = {}
        tDict = {}

        def counter(xDict, xList):
            for element in xList:
                xDict[element] = xList.count(element)

        def count():
            counter(sDict, sList)
            counter(tDict, tList)
        count()

        for element in tDict:
            if element in sDict and tDict[element] != sDict[element]:
                return element
            elif element not in sDict:
                return element
            
#Problem description: https://leetcode.com/problems/find-the-difference/description/ 