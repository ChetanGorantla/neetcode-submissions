class PrefixNode:
    def __init__(self, char=None, children=None, isWord=False):
        self.char=char
        self.isWord = isWord
        self.children = {}

class Solution:
    

    def insert(self, curr: PrefixNode, word: str) -> None:
        #curr = self.root
        for ch in word:
            if ch not in curr.children:
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
        out = []
        # don't keep track of visited because ALL possible states are unique
        # dealing with permutations, not combinations
        def is_empty(node: PrefixNode) -> bool:
            if node.isWord:
                return False
            for child in node.children.values():
                if child is not None:
                    return False
            return True


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def search(r: int, c: int, word: str, parent: PrefixNode):
            if not (r >= 0 and c >= 0 and r < len(board) and c < len(board[r])):
                return
            
            
            
                # don't exit early, could be a word that is a prefix
            
            # branch
            
            curr = parent.children.get(board[r][c])
            temp = board[r][c]
            word += temp
            
            if not curr:
                return
                # no child present, nowhere to go

            
            #print(board[r][c])

            if curr.isWord:
                # this branch is a word, add to the set
                #print(f"{word} is a word")
                out.append(word)
                #avoid duplicate additions
                curr.isWord = False

            # explore all directions from this branch
            board[r][c] = "*"
            for direction in directions:
                search(r+direction[0], c+direction[1], word, curr)
            board[r][c] = temp

            # prune dead branch
            if is_empty(curr):
                parent.children[temp] = None


            return
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                #print(" ")
                search(i,j,"",root)
        
        
        
        return out
            







