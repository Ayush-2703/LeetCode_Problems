class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [False] * n
        complete_count = 0
        
        for i in range(n):
            if not visited[i]:
                v_count = 0
                e_count = 0
                
                def dfs(node):
                    nonlocal v_count, e_count
                    visited[node] = True
                    v_count += 1
                    e_count += len(graph[node])
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            dfs(neighbor)
                
                dfs(i)
                
                if e_count == v_count * (v_count - 1):
                    complete_count += 1
                    
        return complete_count        