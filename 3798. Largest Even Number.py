class Solution:
    def largestEven(self, s: str) -> str:
        for i in range(len(s)-1, -1, -1):
            if s[i]=='1':
                continue
            else:
                return s[0:i+1]
        return ""
        
