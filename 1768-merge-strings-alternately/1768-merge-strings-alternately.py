class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]                          # Create an empty list to store merged characters
        i=0
        while i<len(word1) or i<len(word2):# Loop until both strings are fully traversed
            if i<len(word1):
                result.append(word1[i])
            if i<len(word2):
                result.append(word2[i])    
            i=i+1                          # Move to the next index
        return ''.join(result)             # Convert list to string and return result   
