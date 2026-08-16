class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        count=0
        def dfs(city):
            if city in visited:
                return
            visited.add(city)    

            for next_city in range(len(isConnected)):
                if isConnected[city][next_city]==1:
                    dfs(next_city)

        for city in range(len(isConnected)):
            if city not in visited:
                count+=1
                dfs(city)                

        return count        