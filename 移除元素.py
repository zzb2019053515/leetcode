class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = 0
        slow = 0
        for read in range(len(nums)):
            if (nums[read] != val):
                nums[slow] = nums[read]
                slow = slow + 1  #slow已经是新数组的长度了，因为slow在更新之后加1
        return slow
