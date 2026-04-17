class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        //sort the fleet so that the closest to the target is first
        //hashmap of speeds to positions
        int n = position.length;
        int[][] cars = new int[n][2];
        for (int i = 0; i < n; i++){
            cars[i][0] = position[i];
            cars[i][1] = speed[i];

        }
        Arrays.sort(cars, (a,b) -> Integer.compare(b[0], a[0]));
        //sort in descending order
        int fleets = 1;
        double prevTime = (float)(target - cars[0][0])/(cars[0][1]);
        for (int i = 1; i < n; i++){
            double currTime = (float)(target - cars[i][0])/cars[i][1];
            if (currTime > prevTime){
                fleets++;//if the time for a lower pos car is greater, fleets increase
                prevTime = currTime;
            }
        }
        return fleets;

    }
}
