class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array_length = len(nums)

        for num in range(0, array_length):
            nums.insert((num + array_length), nums[num])

        return nums