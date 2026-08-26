class Solution {
    public int[] buildArray(int[] nums) {
        int[] return_arr = new int[nums.length];
        int i = 0;
        for(int num:nums){
            return_arr[i] = nums[num];
            i++;
        }
        return return_arr;
    }
}