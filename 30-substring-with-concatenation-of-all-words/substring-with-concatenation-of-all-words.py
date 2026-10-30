from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        
        if n < total_len:
            return []
        
        word_freq = Counter(words)
        result = []
        
        # Check each possible offset
        for i in range(word_len):
            left = i
            right = i
            seen = Counter()
            matched_words = 0
            
            while right + word_len <= n:
                w = s[right : right + word_len]
                right += word_len
                
                if w in word_freq:
                    seen[w] += 1
                    matched_words += 1
                    
                    # Shrink from the left if there are duplicate excess occurrences
                    while seen[w] > word_freq[w]:
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        matched_words -= 1
                        left += word_len
                    
                    # Valid concatenated substring found
                    if matched_words == num_words:
                        result.append(left)
                else:
                    # Reset if an invalid word is encountered
                    seen.clear()
                    matched_words = 0
                    left = right
                    
        return result