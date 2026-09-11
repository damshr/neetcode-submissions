class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))) #find string length
            res.append('#')
            res.append(s) #  4#neet
        return "".join(res) #final encoded string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 
            length = int(s[i:j]) #get the length
            i = j + 1 #actual word starts from here
            j = i + length #reach end of word
            res.append(s[i:j]) 
            i = j
        return res