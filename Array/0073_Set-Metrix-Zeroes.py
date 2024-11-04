class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        zero_rows = set()
        zero_cols = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        # 記錄零的位置
        
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0
        # 把行設為零
        
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0
        # 把列設為零

# Runtime 100.00%
# Memory 88.42%
