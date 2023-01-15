#trie structure autocomplete itertion 1

class Trie:
    def __init__(self):
        self.root ={"*":"*"}

    def addWords(self, wrd):
        currentNode = self.root
        for letter in wrd:
            if letter not in currentNode:
             currentNode[letter] = {} 
            currentNode = currentNode[letter]
        currentNode["*"] = "*"
    
    def wordExist(self, wrd):
        currentNode = self.root
        for letter in wrd: 
            if letter not in currentNode:
                return False    
            currentNode = currentNode[letter]
        return "*" in currentNode



trie = Trie()
words = ["Dog","Dogs", "table", "boot", "boots", "booted"]
for word in words:
    trie.addWords(word)