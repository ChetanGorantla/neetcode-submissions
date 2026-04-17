class MinStack {
    private Stack<Integer> regular;
    private Stack<Integer> min;
    public MinStack() {
        regular = new Stack<Integer>();
        min = new Stack<Integer>();
    }
    
    public void push(int val) {
        regular.push(val);
        if (min.isEmpty() || min.peek() >= val){
            min.push(val);
        }
    }
    
    public void pop() {
        if (!regular.isEmpty()){
            int val = regular.pop();
            if (min.peek() == val){
                min.pop();
            }
        }
        
        
        
    }
    
    public int top() {
        return regular.peek();
    }
    
    public int getMin() {
        return min.peek();

    }
}
