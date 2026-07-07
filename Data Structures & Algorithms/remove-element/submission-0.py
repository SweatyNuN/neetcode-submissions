class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        offset = 0
        for num in range(0, len(nums)):
            me_number = nums[num - offset]
            if me_number == val:
                nums.pop(num - offset)
                offset += 1

        return len(nums)