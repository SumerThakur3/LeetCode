class Solution:
    def decodeString(self, s: str) -> str:
        num_stack=[]
        string_stack=[]
        number=0
        current=""
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == "[":
                num_stack.append(number)
                string_stack.append(current)

                number=0
                current=""

            elif ch == "]":
                repeat = num_stack.pop()
                previous = string_stack.pop()

                current = previous + current * repeat
            else:
                current+=ch        
                    
        return current