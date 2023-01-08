class Solution:
    def calPoints(self, operations: List[str]) -> int:
        recordArray = []
        for i in range(len(operations)):
            if(operations[i].isnumeric() or "-" in operations[i]):
                recordArray.append(int(operations[i]))
            elif(operations[i]=="+"):
                recordArray.append(recordArray[len(recordArray)-2]+recordArray[len(recordArray)-1])
            elif(operations[i]=="D"): 
                recordArray.append(recordArray[len(recordArray)-1]*2)
            elif(operations[i]=="C"):
                recordArray.pop(len(recordArray)-1)
        return sum(recordArray)

#Problem description: https://leetcode.com/problems/baseball-game/description/