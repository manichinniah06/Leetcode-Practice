class Solution {
    public void sortColors(int[] nums) {
        int zero_count = 0;
        int one_count = 0;
        int two_count = 0;
        int j = 0;
        for(int i = 0;i<nums.length;i++){
            if(nums[i] == 0){
                zero_count++;
            }
            else if(nums[i] == 1){
                one_count++;
            }
            else if(nums[i] == 2){
                two_count++;
            }
        }
        while(zero_count>0){
            nums[j] = 0;
            j++;
            zero_count--;
        }
        while(one_count>0){
            nums[j] = 1;
            j++;
            one_count--;
        }
        while(two_count>0){
            nums[j] = 2;
            j++;
            two_count--;
        }
    }
}