class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch=="*":
                #removes the element before star(we are not inserting star into stack)
                stack.pop()  
            else :
                stack.append(ch)         
        return ''.join(stack)          
