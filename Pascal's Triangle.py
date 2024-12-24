class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            mylist=[[1],[1,1]]
            for i in range(2,numRows):
                l=[0]*(i+1)
                for j in range(0,i//2+1):
                    if j==0:
                        l[j]=1
                        l[i-j]=1
                    else:
                        l[j]=mylist[i-1][j-1]+mylist[i-1][j]
                        l[i-j]=l[j]
                mylist.append(l)
        return mylist

        
