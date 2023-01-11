class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        mergedArray = nums1+nums2
        mergedArray.sort()
        if(len(mergedArray)%2 != 0):       
            return mergedArray[len(mergedArray)/2]
        if(len(mergedArray)%2 == 0): 
            return (float(mergedArray[len(mergedArray)/2-1]+mergedArray[len(mergedArray)/2])/2)

#Problem description: https://leetcode.com/problems/median-of-two-sorted-arrays/description/