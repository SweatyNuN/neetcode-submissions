class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        while True:
            am_i_done = True

            for index, num in enumerate(nums):
                if num < nums[index - 1] and index != 0:
                    nums[index-1], nums[index] = nums[index], nums[index-1]
                    am_i_done = False
        
            if am_i_done is True:
                return nums
