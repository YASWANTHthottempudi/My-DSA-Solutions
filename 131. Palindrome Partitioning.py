class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def part(index,arr):
            if index==len(s):
                res.append(arr[:])
                return
            
            for i in range(index,len(s)):
                
                if s[index:i+1]==s[index:i+1][::-1]:
                    
                    arr.append(s[index:i+1])
                    part(i+1,arr)
                    arr.pop()
        
        part(0,[])
        return res
        
