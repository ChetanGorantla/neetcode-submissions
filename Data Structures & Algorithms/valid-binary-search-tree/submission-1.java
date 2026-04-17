/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isValidBST(TreeNode root) {
        //dfs
        //need to have ranges for min and max possible value for ur current node based on previous nodes
        //if right subtree, min needs to be value of prev node and max is infinity
        //if left subtree, max needs to be value of prev node and min is -inf
        return dfs(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        

    }
    public boolean dfs(TreeNode root, int l, int r){
        if (root == null){
            return true;
        }
        if (root.val > l && root.val < r){
            return (true && dfs(root.left, l, root.val) && dfs(root.right, root.val, r));

        }else{
            return false;
        }


    }
    
}
