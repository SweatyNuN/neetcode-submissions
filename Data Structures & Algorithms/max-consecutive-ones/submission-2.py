class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter_log = []
        counter = 0

        for num in nums:
            if num == 1:
                counter += 1
            else:
                counter_log.append(counter)
                counter = 0
        counter_log.append(counter)

        return max(counter_log)