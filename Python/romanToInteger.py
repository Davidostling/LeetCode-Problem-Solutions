class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        romanDict = {"I": 1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}   
        for i in range(len(s)-1):
            if romanDict[s[i]] >= romanDict[s[i+1]]:
                integer += romanDict[s[i]] 
            if romanDict[s[i]] < romanDict[s[i+1]]:
                integer -= romanDict[s[i]]
        
        return (integer+romanDict[s[-1]])