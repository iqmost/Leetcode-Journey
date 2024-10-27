class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])

        for i in range(n//2): # 遍歷行
            for j in range(i, n-i-1): # 遍歷列
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = \
                matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]
        # 迴圈先做行(0, 0) (1, 0) (2, 0)，再做下一行(1, 1)
        # Python賦值會先快照等號後面的值，再一次賦值
"""
        n = 4

        觀察matrix[3][3]找規律：

        3 3 < 0 3 < 0 0 < 3 0
        2 3 < 0 2 < 1 0 < 3 1
        1 3 < 0 1 < 2 0 < 3 2
        0 3 < 0 0 < 3 0 < 3 3

        (0, 0) (0, 1) (0, 2) (0, 3) 
        (1, 0) (1, 1) (1, 2) (1, 3) 
        (2, 0) (2, 1) (2, 2) (2, 3) 
        (3, 0) (3, 1) (3, 2) (3, 3)
"""

# Runtime 100.0%
# Memory 64.06%
