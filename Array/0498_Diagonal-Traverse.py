class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row=len(mat)
        col=len(mat[0])
        (x, y) = (0, 0)
        ans = []

        # 右上(-1, 1)
        # 右(0, 1)
        # 左下(1, -1)
        # 下(1, 0)

        for _ in range(row*col):
            ans.append(mat[x][y])
            if (x+y) % 2:
                if x == row-1: # 黃色，到最底下只能往右
                    y += 1
                elif y == 0: # 黃色，到最左邊只能往下
                    x += 1
                else: # 黃色，一般往左下
                    x += 1; y -= 1
            else:
                if y == col-1: # 褐色，到最右邊只能往下
                    x += 1
                elif x == 0: # 褐色，到最上面只能往右
                    y += 1
                else: # 褐色，一般往右上
                    x -= 1; y += 1

        return ans

# Runtime 99.76%
# Memory 91.65%
