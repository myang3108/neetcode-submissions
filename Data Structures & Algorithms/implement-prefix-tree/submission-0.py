class PrefixTree:

    # use nested hashmaps to represent each letter layer

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        
        for c in word:
            if c not in d:
                d[c] = {} # make a new dictionary if we havent seen it before - mark it as seen
            
            d = d[c] # get more nested so we can do the next letter of the word
        
        d['.'] = '.' # mark the end



    def search(self, word: str) -> bool:
        d = self.trie
        for c in word:
            if c not in d:
                return False
            else:
                d = d[c]
        return '.' in d
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            else:
                d = d[c]
        return True
        
        