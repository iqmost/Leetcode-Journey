class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer=[1 for _ in range(n)]
        # 宣告長度為 n 的 [1, 1, 1...] 陣列

        left=1
        for i in range(0, n):
            answer[i] *= left
            left *= nums[i]
        # 迭乘左邊的元素

        right=1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        # 迭乘右邊的元素，從首元素 n-1 到尾元素 -1 (不含)，迭代-1

        return answer

# Runtime 96.43%
# Memory 94.16%
