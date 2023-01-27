class Solution:
    def isHappy(self, n: int) -> bool:
        counter = 0

        def recursion(n, counter):
            counter+=1
            sum = 0
            for element in str(n):
                sum += int(element)**2
            if(sum == 1):
                return True
            if(sum != 1 and counter == 8):
                return False 
            else:
                return recursion(sum, counter)            

        return recursion(n, counter)

#Problem description: https://leetcode.com/problems/happy-number/description/