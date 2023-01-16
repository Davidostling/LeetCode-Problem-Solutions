class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalArray = []
        tempArray = []
        numRows = rowIndex+1

        for i in range(1, numRows+1):
            for j in range(i):
                tempArray.append(1)
            pascalArray.append(tempArray)
            tempArray = []
        
        for i in range(len(pascalArray)-1):
            for j in range(len(pascalArray[i])-1):
                pascalArray[i+1][j+1] = pascalArray[i][j] + pascalArray[i][j+1]
        return pascalArray[len(pascalArray)-1]

#Problem description https://leetcode.com/problems/pascals-triangle-ii/description/