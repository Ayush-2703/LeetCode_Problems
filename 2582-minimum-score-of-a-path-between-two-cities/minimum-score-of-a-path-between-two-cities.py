class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        ans = float('inf')
        visited = [False] * (n + 1)
        visited[1] = True
        q = deque([1])
        
        while q:
            u = q.popleft()
            for v, w in graph[u]:
                if w < ans:
                    ans = w
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    
        return ans