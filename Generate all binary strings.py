#User function Template for python3

class Solution:
    def generateBinaryStrings(self, n):
        # Code here
        res=[]
        def bin( s):
            if len(s)==n:
                res.append(s)
                return
            if len(s)>0:
                if s[-1]=="0":
                    bin(s+"0")
                    bin(s+"1")
                else:
                    bin(s+"0")
            else:
                bin("0")
                bin("1")
        bin("")
        return res
