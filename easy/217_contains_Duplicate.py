"""
Problem 217: Contains Duplicate
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1]):
                return True
        return False
    