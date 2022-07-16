class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> map = new HashSet<>();
        
        for(int r =0; r<9;r++){
            for(int c =0; c<9;c++){
                if (board[r][c] != '.'){
                    if (map.contains("row" + r + board[r][c]) || map.contains("col" + c + board[r][c])){
                        return false;
                    }
                    map.add("row" + r + board[r][c]);
                    map.add("col" + c + board[r][c]);
                    
                    if(map.contains("box" + (r/3) + (c/3) + board[r][c])){
                        return false;
                    }
                    map.add("box" + (r/3) + (c/3) + board[r][c]);
                }
            }
        }
        return true;
    }
}