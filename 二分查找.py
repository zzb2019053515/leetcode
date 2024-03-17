##1.暴力解法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if (nums[i] == target):
                return i
        if (i == (len(nums)-1)):
            return -1
##2.二分法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left <= right:
            mid  = (right - left)//2 + left
            if (nums[mid] == target):
                return mid
            if (nums[mid] > target):
                right = mid - 1
            if  (nums[mid]< target):
                left = mid + 1
        if (left>right):
            return -1
