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
    public int kthSmallest(TreeNode root, int k) {
        //look at left subtree, then current node, then right subtree
        //in order traversal
        ArrayList<Integer> arr = new ArrayList<>();
        dfs(root, arr);
        return arr.get(k-1);//gets kth value
        

    }
    public void dfs(TreeNode root, List<Integer> arr){
        //update an array from inorder traversal
        //dfs left, attach current node, dfs right
        //itll trickle down
        if (root == null){
            return;//if node is null that means our previous one had no children to this side
        }
        dfs(root.left, arr);
        arr.add(root.val);
        dfs(root.right, arr);

    }
    
}
