class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_length = len(nums) / 2

        return sorted(nums)[math.floor(half_length)]