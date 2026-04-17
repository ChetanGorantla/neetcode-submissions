class PrefixNode:
    def __init__(self, char=None, children=None, isWord=False):
        self.char=char
        self.isWord = isWord
        self.children = {}
        for i in range(ord('a'), ord('z')+1):
            self.children[chr(i)] = None

class PrefixTree:
    # each node needs to have 26 children?
    # we don't care about storing the actual data
    # we just care about storing whether or not that prefix exists in the trie
    # so we can just store the characters as a sequence of node children
    # there should be a hashmap of children
    # {character: node}

    # the character links to the next node
    

    # the initial root should be a sentinel (have nothing as the current char)
    # but be used to redirect to the children
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if curr.children[ch] is None:
                curr.children[ch] = PrefixNode(ch)
            curr = curr.children[ch]
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if curr.children[ch] is None:
                return False
            curr = curr.children[ch]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if curr.children[ch] is None:
                return False
            curr = curr.children[ch]
        return True
        

        
        