class Solution {
    public boolean exist(char[][] board, String word) {
        // locate all starting positions
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[i].length; j++){
                if (board[i][j] == word.charAt(0)){
                    HashSet<List<Integer>> visited = new HashSet<>();
                    if (wordSearch(board, word, 0, i, j, visited)){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean wordSearch(char[][] board, String word, int idx, int r, int c, HashSet<List<Integer>> visited){
        if (idx == word.length()){
            return true;
        }
        if (idx > word.length()){
            return false;
        }
        
        // make sure we not out of bounds
        if (r >= 0 && r < board.length && c >= 0 && c < board[0].length){
            // make sure we not visited already
            ArrayList<Integer> coords = new ArrayList<>();
            coords.add(r);
            coords.add(c);
            if (visited.contains(coords)){
                return false;
            }

            // not visited before
            char currChar = board[r][c];
            visited.add(coords);
            if (currChar == word.charAt(idx)){
                // continue searching
                if (wordSearch(board, word, idx+1, r+1, c, visited) || 
                wordSearch(board, word, idx+1, r, c+1, visited) ||
                wordSearch(board, word, idx+1, r, c-1, visited) ||
                wordSearch(board, word, idx+1, r-1, c, visited)){
                    return true;
                }
                visited.remove(coords);
            }else{
                visited.remove(coords);
                return false;
            }
        }

        return false;
        
        
    }
}
