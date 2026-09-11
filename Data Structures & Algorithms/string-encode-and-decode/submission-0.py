class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "" #return empty string
        sizes,res = [],[] #sizes lits will store sizes of each string
        for s in strs:
            sizes.append(len(s))#add length
        for sz in sizes: #put the sizes in res
            res.append(str(sz)) #write all size sep by comma 4, ,4, ,4,
            res.append(',')
        res.append('#') #marks end of string
        res.extend(strs) # add actual string after #
        return ''.join(res) #4,4,4,#neetcodelove
        
    def decode(self, s: str) -> List[str]:
        if not s: #if encoded string is empty
            return []
        sizes,res,i = [],[],0
        while s[i] != '#': #parse each size till comma
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz]) #read that many chars, append to res
            i += sz 
        return res
