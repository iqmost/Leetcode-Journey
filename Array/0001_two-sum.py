class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        a, b = 0, len(sortedNums)-1
        while a < b:
            if target < (sortedNums[a]+sortedNums[b]):
                b-=1
            elif target > (sortedNums[a]+sortedNums[b]):
                a+=1
            else:
                break


        hasA=False
        for i in range(len(nums)):
            if nums[i] == sortedNums[a] and not hasA:
                A=i
                hasA = True
            elif nums[i] == sortedNums[b]:
                B=i

        return A, B

        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
        """
# 1: Double Looping
# 2: Data Arranged