class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trackingArray = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j] == target:
                        trackingArray.append([i, j])
        return (trackingArray[0])

#Problem description: https://leetcode.com/problems/two-sum/description/