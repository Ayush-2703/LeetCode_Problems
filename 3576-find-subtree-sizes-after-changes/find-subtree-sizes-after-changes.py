class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_children: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            orig_children[parent[i]].append(i)

        new_parent = parent[:]
        # Stack of ancestor indices per character ('a' - 'z') along current DFS path
        last_seen: List[List[int]] = [[] for _ in range(26)]

        def find_new_parents(u: int) -> None:
            c = ord(s[u]) - ord("a")
            last_seen[c].append(u)

            for v in orig_children[u]:
                find_new_parents(v)

            last_seen[c].pop()
            if last_seen[c]:
                new_parent[u] = last_seen[c][-1]

        find_new_parents(0)

        new_children: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        def subtree_size(u: int) -> int:
            size = 1
            for v in new_children[u]:
                size += subtree_size(v)
            ans[u] = size
            return size

        subtree_size(0)
        return ans