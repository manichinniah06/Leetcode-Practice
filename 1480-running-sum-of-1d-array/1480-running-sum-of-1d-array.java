class Solution {
    public int[] runningSum(int[] nums) {
        int[] return_arr = new int[nums.length];
        for(int i = 0;i < nums.length;i++){
            int sum = 0;
            for(int j = 0;j<=i;j++){
                sum = sum + nums[j];
            }
            return_arr[i] = sum;
        }
        return return_arr;
    }
}