class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]

            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b,value))
            graph[b].append((a,1/value))       

        def dfs(current,target,visited):
            if current == target:
                return 1.0
            visited.add(current)

            for next_var,value in graph[current]:
                if next_var not in visited:
                    answer=dfs(next_var,target,visited)

                    if answer != -1.0:
                        return value*answer

            return -1.0
        answer=[]

        for a,b in queries:
            if a not in graph or b not in graph:
                answer.append(-1.0)
            else:
                answer.append(dfs(a,b,set()))

        return answer                                


