class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result=[]
        j=0
        for i in range(len(t)):
                 if j<len(s) and t[i]==s[j]:
                     result.append(t[i])
                     j+=1
        return ''.join(result)==s            