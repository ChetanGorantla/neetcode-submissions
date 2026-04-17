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
    //search for both nodes
    
    //in your search, identify the lowest value among the values before they split
    //basically recurse until you have to split 
    //when you find where you have to split (where p and q are not in the same side of the node)
    //you will have to return the current minimum
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || p == null || q == null){
            return null;
        }
        if (Math.min(p.val, q.val) > root.val){//smallest falls to the right
            return lowestCommonAncestor(root.right, p, q);
        }else if (Math.max(p.val, q.val) < root.val){//largest falls to the left
            return lowestCommonAncestor(root.left, p, q);
        }else{//smallest and largest are on opposing sides, we found the break point
            return root;
        }
    }
    //NOT LEAST, LOWEST!!
}
