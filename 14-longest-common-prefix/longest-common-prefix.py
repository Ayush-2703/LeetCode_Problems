class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        first_str = strs[0]
        for i, char in enumerate(first_str):
            for other in strs[1:]:
                if i >= len(other) or other[i] != char:
                    return first_str[:i]
                    
        return first_str