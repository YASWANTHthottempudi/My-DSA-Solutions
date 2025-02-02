class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        l1=[]
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    l1=[nums[i],nums[j],nums[k]]
                    l.append(l1)
                    j+=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k-1]):
                        k-=1
        return l
