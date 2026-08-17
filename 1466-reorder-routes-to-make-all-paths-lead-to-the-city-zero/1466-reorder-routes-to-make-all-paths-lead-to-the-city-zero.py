class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=[[]for _ in range(n)]    #This creates an empty list for every city.

        for a,b in connections:
            graph[a].append((b,1))     #Store the original road
            graph[b].append((a,0))     #Store the opposite direction

        visited=set()
        count=0
        def dfs(city):
            nonlocal count  
            #nonlocal count allows DFS to modify the count created outside DFS.

            visited.add(city)

            for next_city,direction in graph[city]:
                if next_city not in visited:
                    if direction==1:
                        count+=1
                    dfs(next_city)        
        dfs(0)
        return count