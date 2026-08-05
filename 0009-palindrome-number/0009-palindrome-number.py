class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:                        # Negative numbers cannot be palindromes
            return False
        temp=x                         # Store original number for comparison
        rev=0
        while x!=0 :                   # Loop until all digits are processed
            rev= rev * 10 + x % 10     # Add last digit of x to rev
            x = x//10                  # Remove last digit from x
        return temp == rev