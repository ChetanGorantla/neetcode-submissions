class Solution {
    public int calPoints(String[] operations) {
        int score = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < operations.length; i++){
            if (operations[i].equals("+")){
                int one = stack.pop();
                int two = stack.pop();
                stack.push(two);
                stack.push(one);
                stack.push(one+two);
                score+=(one+two);
            }else if (operations[i].equals("C")){
                int removal = stack.pop();
                score-=removal;
            }else if (operations[i].equals("D")){
                int dbl = 2 * stack.peek();
                score+=dbl;
                stack.push(dbl);
            }else{
                int add = Integer.parseInt(operations[i]);
                stack.push(add);
                score+=add;
            }
        }
        return score;

    }
}