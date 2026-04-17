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
    public List<Integer> rightSideView(TreeNode root) {
        //cant really use dfs cuz you can have a left node that is returned also
        //use bfs
        //   5
        //  /
        // 3
        List<Integer> out = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()){
            int qlen = q.size();
            TreeNode rightside = null; //you keep one rightside for each queue iteration (each level)
            for (int i = 0; i < qlen; i++){
                TreeNode node = q.poll();
                if (node != null){
                    rightside = node;
                    q.add(node.left);
                    q.add(node.right);
                    
                }
                
                
            }
            //once all the nodes of the current level have been iterated upon, the final value of rightside is the true right side because we kept updating within the current level
            if (rightside != null){
                out.add(rightside.val);
            }
            
            
        }
        return out;
        
        
    }
}
