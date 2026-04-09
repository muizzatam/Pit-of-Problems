# return True if the given array contains a duplicate element


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if i in map:
                return True
            else:
                map[i] = 1
        return False
