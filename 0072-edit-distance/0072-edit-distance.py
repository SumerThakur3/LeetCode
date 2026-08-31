class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)

        dp=[[0]*(m+1) for _ in range(n+1)]
        
        # If word2 is empty, delete all characters from word1
        for i in range(n+1):
            dp[i][0]=i
        # If word1 is empty, insert all characters of word2
        for j in range(m+1):
            dp[0][j]=j

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1] #No operation needed.
                else:
                    #dp[i][j] = 1 + min(delete, insert, replace)
                    dp[i][j]=1+min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )    

        return dp[n][m]            
        