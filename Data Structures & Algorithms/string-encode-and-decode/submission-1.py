class Solution:

    def encode(self, strs: List[str]) -> str:
        # have the length of the current word and then a delimiter before the word
        res = ""
        for word in strs:
            res += str(len(word)) + "*" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        # read the len of the following string before we reach the delimiter
        i,j = 0,0
        final = []
        while i < len(s):
            j = i
            while (s[j] != '*'):
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            final.append(s[i:j])
            i = j
        
        return final



            
