class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:

        if p1 == p2 == p3 == p4:
            return False
        
        def dist(p, q):
            x1, y1, x2, y2 = p[0], p[1], q[0], q[1]
            return (y2 - y1) ** 2 + (x2 - x1) ** 2
        
        dists = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p3, p4), dist(p2, p4), dist(p2, p3)]
        dists.sort()

        if dists[0] == dists[1] == dists[2] == dists[3]:
            if dists[4] == dists[5]:
                return True
        return False
