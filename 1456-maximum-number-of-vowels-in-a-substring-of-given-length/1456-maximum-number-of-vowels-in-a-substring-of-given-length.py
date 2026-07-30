class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v=set('aeiou')
        count=0
        for i in range(k):
            if s[i] in v:
                count+=1
        max_vowels=count
        for i in range(k,len(s)):
            if s[i] in v:           # add new character
                count+=1
            if s[i-k] in v:         # remove old character
                count-=1
            if count > max_vowels:
                max_vowels=count
        return max_vowels      