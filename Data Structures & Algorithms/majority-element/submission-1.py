class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        muhdata = dict()

        for num in nums:
            if num in muhdata:
                muhdata[num] += 1
            else:
                muhdata[num] = 1

        return max(muhdata, key=lambda k: muhdata[k])