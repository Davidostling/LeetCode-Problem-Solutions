class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        checkerString = ""
        for i in range(len(str(x)), 0, -1):   

            checkerString += str(x)[i-1]
            
        if(checkerString == str(x)):
            return True

