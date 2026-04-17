class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        //binary search thru the first element of each row
        //binary search thru each element in that row
        if (matrix.length == 1 && matrix[0].length == 1){
            if (matrix[0][0] == target){
                return true;
            }else{
                return false;
            }
        }
        int l = 0;
        int r = matrix.length-1;
        int row = 0;
        while (l <= r){
            int middle = (l+r)/2;
            
            
            System.out.println("Current index at " + middle);
            if (target > matrix[middle][0]){
                l = middle+1;
                row = middle;
                
            }else if (target < matrix[middle][0]){
                r = middle-1;
                row = middle-1;
                
            }else if (target == matrix[middle][0]){
                
                return true;
            }
        }
        if (row < 0 || row > matrix.length-1){
                return false;
            }
        System.out.println("Found row " + row);
        //binary search the row
        l = 0;
        r = matrix[row].length-1;
        while (l <= r){
            int middle = (l+r)/2;
            if (target > matrix[row][middle]){
                l = middle+1;

            }else if (target < matrix[row][middle]){
                r = middle-1;
            }else if (target == matrix[row][middle]){
                return true;
            }
        }
        return false;
        
    }
}
