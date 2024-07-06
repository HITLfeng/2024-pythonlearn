class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        retStr = ""
        while columnNumber / 26 > 0:
            retStr += chr(columnNumber % 26)



# A B ... Z
# AA AB AC ... ZY ZZ
# AAA AAB AAC ...

s = Solution()
print(s.convertToTitle(1))