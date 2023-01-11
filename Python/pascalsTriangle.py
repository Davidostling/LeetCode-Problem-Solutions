class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalArray = []
        tempArray = []
        
        for i in range(1, numRows+1):
            for j in range(i):
                tempArray.append(1)
            pascalArray.append(tempArray)
            tempArray = []
        
        for i in range(len(pascalArray)-1):
            for j in range(len(pascalArray[i])-1):
                pascalArray[i+1][j+1] = pascalArray[i][j] + pascalArray[i][j+1]
        
        return pascalArray

