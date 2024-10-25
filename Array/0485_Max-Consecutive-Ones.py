class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        ans = 0
        for i in nums:
            if i == 1:
                n += 1
                ans = max(ans, n)
            else:
                n = 0
        return ans

# Runtime 96.23%
# Memory 9.77%
