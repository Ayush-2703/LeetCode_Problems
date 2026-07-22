import bisect
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        
        total_ones = s.count('1')
        
        Z = []
        lengths = []
        curr = 0
        
        for block in s.split('1'):
            b_len = len(block)
            if b_len > 0:
                Z.append((curr, curr + b_len - 1))
                lengths.append(b_len)
            curr += b_len + 1
            
        m = len(Z)
        
        if m > 1:
            pair_sum = [lengths[j] + lengths[j+1] for j in range(m - 1)]
            LOG = (m - 1).bit_length()
            
            st = [pair_sum]
            for k in range(1, LOG):
                length = 1 << (k - 1)
                prev = st[-1]
                
                st.append([
                    prev[j] if prev[j] > prev[j + length] else prev[j + length] 
                    for j in range(len(prev) - length)
                ])
                           
            def query_st(L: int, R: int) -> int:
                k = (R - L + 1).bit_length() - 1
                row = st[k]
                left_val = row[L]
                right_val = row[R - (1 << k) + 1]
                return left_val if left_val > right_val else right_val
                
        ends = [g[1] for g in Z]
        starts = [g[0] for g in Z]
        
        ans = [0] * len(queries)
        for qi, (l, r) in enumerate(queries):
            
            if m < 2:
                ans[qi] = total_ones
                continue
            
            a = bisect.bisect_left(ends, l)
            b = bisect.bisect_right(starts, r) - 1
            
            gain = 0
            if a < b:
                
                len_a = Z[a][1] - l + 1 if Z[a][0] < l else lengths[a]
                len_b = r - Z[b][0] + 1 if Z[b][1] > r else lengths[b]
                
                if a + 1 == b:
                    gain = len_a + len_b
                else:
                   
                    gain = len_a + lengths[a+1]
                    alt = lengths[b-1] + len_b
                    if alt > gain: 
                        gain = alt
                    
                    if a + 1 <= b - 2:
                        internal = query_st(a + 1, b - 2)
                        if internal > gain: 
                            gain = internal
                        
            ans[qi] = total_ones + gain
            
        return ans