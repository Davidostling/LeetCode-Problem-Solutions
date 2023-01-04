class Solution {
    public boolean isPowerOfTwo(int n) {
        boolean foundBool = false;
        for (int i = 0; i <= n; i++) {
            double poweredNumber = Math.pow(2, i);
            if (poweredNumber == n) {
                foundBool = true;
                break;
            } else if (poweredNumber > n) {
                foundBool = false;
                break;
            }
        }
        return foundBool;
    }
    // Problem description: https://leetcode.com/problems/power-of-two/description/
}