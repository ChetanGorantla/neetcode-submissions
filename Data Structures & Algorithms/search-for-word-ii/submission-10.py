class PrefixNode:
    def __init__(self, char=None, children=None, isWord=False):
        self.char=char
        self.isWord = isWord
        self.children = {}
        for i in range(ord('a'), ord('z')+1):
            self.children[chr(i)] = None

class Solution:
    

    def insert(self, curr: PrefixNode, word: str) -> None:
        #curr = self.root
        for ch in word:
            if curr.children[ch] is None:
                curr.children[ch] = PrefixNode(ch)
            curr = curr.children[ch]
        curr.isWord = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make a trie as the overall "searching window"
        # recursively branch into the trie as we find more characters befitting
        # branch into children nodes and recurse
        root = PrefixNode()
        # start root at null node   
        for word in words:
            self.insert(root, word)
        
        # backtrack on all parts of the grid
        located = set()
        out = []
        # don't keep track of visited because ALL possible states are unique
        # dealing with permutations, not combinations

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def search(r: int, c: int, word: str, curr: PrefixNode):
            if not (r >= 0 and c >= 0 and r < len(board) and c < len(board[r])):
                return
            
            
            
                # don't exit early, could be a word that is a prefix
            
            # branch
            
            curr = curr.children.get(board[r][c])
            temp = board[r][c]
            word += temp
            
            if not curr:
                return
                # no child present, nowhere to go

            
            #print(board[r][c])

            if curr.isWord and word not in located:
                # this branch is a word, add to the set
                #print(f"{word} is a word")
                out.append(word)
                located.add(word)

            # explore all directions from this branch
            board[r][c] = "*"
            for direction in directions:
                search(r+direction[0], c+direction[1], word, curr)
            board[r][c] = temp

            
            return
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                #print(" ")
                search(i,j,"",root)
        
        
        
        return out
            







