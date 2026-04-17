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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null){
            return new TreeNode(val);
        }
        dfs(root, val, null, false, false);
        return root;
    }
    public void dfs(TreeNode root, int val, TreeNode prev, boolean left, boolean right){
        if (root == null){
            TreeNode insertedNode = new TreeNode(val);
            if (left){
                prev.left = insertedNode;
            }else{
                prev.right = insertedNode;
            }
            return;
        }
        if (root.val > val){
            prev = root;
            left = true;
            right = false;
            dfs(root.left, val, prev, left, right);
        }else if (root.val < val){
            prev = root;
            right = true;
            left = false;
            dfs(root.right, val, prev, left, right);
        }
    }
}