class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d={}
        s2=""
        for i in s:
            if i not in d:
                d[i]=1
                s2+=i
            else:
                d[i]+=1
        d2={}
        for i in s2:
            if d[i] not in d2:
                d2[d[i]]=i
            else:
                d2[d[i]]+=i
        print(d2)
        count=0
        size=0
        l=[]
        for key, value in d2.items():
            if len(value)>size:
                l.append(value)
                count=key
                size=len(value)
            elif len(value)==size:
                if key>count:
                    l.append(value)
                    count=key
        return l[-1]
