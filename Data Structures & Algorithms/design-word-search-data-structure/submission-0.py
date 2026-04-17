class PrefixNode:
    def __init__(self, char=None, children=None, isWord=False):
        self.char=char
        self.isWord = isWord
        self.children = {}
        for i in range(ord('a'), ord('z')+1):
            self.children[chr(i)] = None

class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if curr.children[ch] is None:
                curr.children[ch] = PrefixNode(ch)
            curr = curr.children[ch]
        curr.isWord = True
    
    def recursiveSearch(self, idx: int, word: str, curr: PrefixNode):
        if curr is None:
            return False
        
        # base case met
        if idx == len(word):
            return curr.isWord

        ch = word[idx]
        # look at children
        located = False
        if ch == '.':
            for child in curr.children:
                located = located or self.recursiveSearch(idx+1, word, curr.children[child])
        else:
            located = self.recursiveSearch(idx+1, word, curr.children[ch])
        return located


    def search(self, word: str) -> bool:
        curr = self.root

        return self.recursiveSearch(0, word, curr)
    