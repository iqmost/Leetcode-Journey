class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        current_sum = 0
        for i in range(len(nums)):
            if current_sum*2 + nums[i] == total_sum:
                return i
            else:
                current_sum += nums[i]
                i += 1
        return -1

# Runtime 94.87%
# Memory 99.39%
