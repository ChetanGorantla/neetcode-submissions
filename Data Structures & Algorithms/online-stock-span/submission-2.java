class StockSpanner {
    //define two stacks
    public Stack<Integer> prices;
    public Stack<Integer> reference_prices;
    public StockSpanner() {
        prices = new Stack<>();
        reference_prices = new Stack<>();
    }
    
    public int next(int price) {
        int count = 1;
        //System.out.println(reference_prices);
        
        while (!reference_prices.empty() && reference_prices.peek() <= price){
            reference_prices.pop();
            count++;
        }
        
        prices.push(price);
        //reference_prices.push(price);
        reference_prices = (Stack<Integer>) prices.clone();
        return count;
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */