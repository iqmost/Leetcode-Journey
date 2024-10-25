class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                n += 1
                if max < n:
                    max = n
            else:
                n = 0
        return max

# Runtime 98.11%
# Memory 9.77%
