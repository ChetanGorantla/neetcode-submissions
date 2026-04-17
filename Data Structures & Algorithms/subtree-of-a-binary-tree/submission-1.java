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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null){
            return false;
        }
        if (subRoot == null){
            return true;
        }

        //we basically go until the subRoot is null because that means all the previous ones we've checked pass the matching

        if (isSameTree(root, subRoot)){
            return true;//initial check
        }
        //actual method of recursing
        //if the left part of our current node or right part of our current node matches the subtree return true
        return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot));


    }
    public boolean isSameTree(TreeNode root, TreeNode subRoot){
        //if both trees are null, theyre both matching
        if (root == null && subRoot == null){
            return true;
        }
        //if both are not null but both values match then we go thru left and right nodes of both so that we can determine if they truly match or not
        if (root != null && subRoot != null && root.val == subRoot.val){
            return isSameTree(root.left, subRoot.left) && isSameTree(root.right, subRoot.right);
        }
        return false;
    }
}
