# return the list containing the indices of the two elements from a given list that sum up to a given target element. You can assume that there will be ecactly one solution for a list and a target.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        p0 = 0
        p1 = 1

        while True:
            if nums[p0] + nums[p1] == target:
                return [p0, p1]
            elif p1 == len(nums) - 1:
                p0 += 1
                p1 = p0 + 1
            else:
                p1 += 1
