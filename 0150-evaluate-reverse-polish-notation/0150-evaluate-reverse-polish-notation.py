class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators={'+','-','*','/'}
        stack=[]

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()

                if i == '+':
                    stack.append(b+a) 

                elif i == '-':
                    stack.append(b-a)

                elif i == '*':
                    stack.append(b*a)

                elif i == '/':
                    stack.append(int(b/a))  

        return stack[-1]                             