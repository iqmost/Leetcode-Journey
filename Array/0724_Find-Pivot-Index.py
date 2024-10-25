class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        current_sum = 0
        for i in range(len(nums)):
            if current_sum*2 + nums[i] == total_sum:
                return i
            current_sum += nums[i]
        return -1

# Runtime 97.83%
# Memory 97.41%
