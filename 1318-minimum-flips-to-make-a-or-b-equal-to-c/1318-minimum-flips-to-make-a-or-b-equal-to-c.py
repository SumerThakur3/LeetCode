class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0

        while a>0 or b>0 or c>0:
            # a&1 gets the last bit of 'a'
            bit_a = a&1 
            bit_b = b&1
            bit_c = c&1
            #if c=0 then a and b should also be zero(according to OR)
            if bit_c == 0:
                count += bit_a + bit_b
            else:
                #if c=1 then a or b should also be 1
                if bit_a == 0 and bit_b == 0:
                    count+=1
            # a>>1 removes the last bit
            a = a>>1
            b = b>>1
            c = c>>1

        return count              
        