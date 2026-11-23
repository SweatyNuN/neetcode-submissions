class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #filtered = list(filter(lambda x: x <= target, nums))
        for x, x_value in enumerate(nums):
            start = x+1
            for y, y_value in enumerate(nums[start:], start=start):
                if x_value + y_value == target:
                    return [x, y]