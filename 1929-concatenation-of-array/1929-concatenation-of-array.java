class Solution {
    public int[] getConcatenation(int[] nums) {
        int req_length = 2*(nums.length);
        int[] return_arr = new int[req_length];
        int i = 0;
        while(i<nums.length){
            return_arr[i] = nums[i];
            i++;
        }
        int j = 0;
        while(i<req_length){
            return_arr[i] = nums[j];
            j++;
            i++;
        }
        return return_arr;
    }
}