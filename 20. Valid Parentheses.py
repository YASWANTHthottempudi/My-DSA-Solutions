class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="{" or i=="(" or i=="[":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if i==')' and stack[-1]!="(":
                    return False
                elif i==']' and stack[-1]!="[":
                    return False
                elif i=='}' and stack[-1]!="{":
                    return False
                else:
                    if stack:
                        stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
        
