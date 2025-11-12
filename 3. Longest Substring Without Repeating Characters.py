class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        count=0
        maxi=0
        j=0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                if d[s[i]]>=j:
                    j=d[s[i]]+1
                d[s[i]]=i
            maxi=max(maxi,i-j+1)
            
        return maxi
        
