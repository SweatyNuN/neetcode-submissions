class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[math.floor(len(nums) / 2)]