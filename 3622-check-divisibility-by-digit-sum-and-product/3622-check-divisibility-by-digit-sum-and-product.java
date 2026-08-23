class Solution {
    public boolean checkDivisibility(int n) {
        int sum = 0;
        int product = 1;
        int initial = n;
        while(n>0){
            int digit = n%10;
            n = n/10;
            sum += digit;
            product *= digit;
        }
        int divisor = sum + product;
        if(initial % divisor == 0){
            return true;
        }
        return false;
    }
}