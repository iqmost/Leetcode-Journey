class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # 移動次數大於陣列大小時

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

        """
        print(self.reverse(nums, 0, n-1))
        print(self.reverse(nums, 0, k-1))
        print(self.reverse(nums, k, n-1))
        print(nums)
        """
    
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        # 自定義函式，指定位置矩陣反轉
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left+=1
            right-=1

# Runtime 94.12%
# Memory 92.10%
