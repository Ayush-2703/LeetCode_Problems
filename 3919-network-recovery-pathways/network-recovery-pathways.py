class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        min_w, max_w = inf, -inf
        
        for u, v, w in edges:
            if online[u] and online[v]:
                g[u].append((v, w))
                min_w = min(min_w, w)
                max_w = max(max_w, w)
                
        if min_w == inf:
            return -1

        def check(mid: int) -> bool:
            dist = [inf] * n
            dist[0] = 0
            pq = [(0, 0)]
            
            while pq:
                d, u = heappop(pq)
                
                if d > k:
                    return False
                if u == n - 1:
                    return True
                if dist[u] < d:
                    continue
                    
                for v, w in g[u]:
                    if w >= mid and d + w < dist[v]:
                        dist[v] = d + w
                        heappush(pq, (dist[v], v))
                        
            return False

        ans = -1
        l, r = min_w, max_w
        
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
                
        return ans