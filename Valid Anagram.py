from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count_frequency(s):
            freq = defaultdict(int)
            for c in s:
                freq[c] += 1
                
            return freq
        
        freq1 = count_frequency(s)
        freq2 = count_frequency(t)
        
        for c in "abcdefghijklmnopqrstuvwxyz":
            if freq1[c] != freq2[c]:
                return False
            
        return True
        