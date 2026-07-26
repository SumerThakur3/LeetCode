class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()  #Automatically removes extra spaces and Converts the string into a list of words
        words.reverse()  #Reverses the order of the words
        return " ".join(words) #Joins words with exactly one space and convert list to string