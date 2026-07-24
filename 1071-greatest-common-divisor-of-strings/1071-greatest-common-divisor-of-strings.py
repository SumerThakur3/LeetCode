class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenation order differs, no common divisor string exists
        if str1+str2!=str2+str1:  
            return ""
        else:
            def gcd(a,b):         #function to find the greatest common divisor (GCD)
                while b:                 #Run the loop until b becomes 0
                    a , b = b , a%b    #b=remainder i.e a%b (Euclidean Algorithm)
                return a               #when b=0 previous value is in a so return a 
        lenght=gcd(len(str1),len(str2)) #len("ABCABC")=6 & len("ABC")= 3 & GCD(6,3)=3
        return str1[:lenght]        #prefix of str1 