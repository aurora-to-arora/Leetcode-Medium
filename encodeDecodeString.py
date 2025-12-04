class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. read length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            
            # 2. read the actual string
            j += 1  # skip '#'
            word = s[j: j + length]
            res.append(word)
            
            i = j + length
        
        return res
