class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        
        for i, n in enumerate(nums):
            if n in seen:
                if abs(i-seen[n]) <= k:
                    return True
            seen[n] = i
        return False