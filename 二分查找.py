##1.暴力解法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if (nums[i] == target):
                return i
        if (i == (len(nums)-1)):
            return -1
