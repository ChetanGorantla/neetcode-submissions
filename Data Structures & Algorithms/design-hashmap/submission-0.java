class MyHashMap {
    public ArrayList<int[]> arr;
    public MyHashMap() {
        arr = new ArrayList<>();
    }
    
    public void put(int key, int value) {
        int[] temp = {key, value};

        for (int[] t: arr){
            if (t[0] == key){
                arr.remove(t);
                break;
            }
        }
        arr.add(temp);
    }
    
    public int get(int key) {
        for (int[] t: arr){
            if (t[0] == key){
                return t[1];
            }
        }
        return -1;
    }
    
    public void remove(int key) {
        for (int[] t: arr){
            if (t[0] == key){
                arr.remove(t);
                break;
            }
        }
    }
    
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */