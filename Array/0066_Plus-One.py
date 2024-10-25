class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        n = len(digits) - 1
        digits[n] += 1
        # 陣列前面補0後，最後一位數直接加一

        for i in range(n):
            if digits[n-i] == 10:
                digits[n-i] = 0
                digits[n-i-1] += 1
                i += 1
            #從尾部遍歷陣列，如果有10就進位
            else:
                break
              
        if digits[0]==0:
            return digits[1:]
            #最後把陣列前面補的0拿掉
        else:
            return digits

# Runtime 100.00%
# Memory 9.74%
