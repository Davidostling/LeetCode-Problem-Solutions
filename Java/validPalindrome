class Solution {
    public boolean isPalindrome(String s) {
        String formattedS = s.replaceAll("\\s", "").replaceAll("[^a-zA-Z0-9\\s+]", "").toLowerCase();
        String reversed = new StringBuilder(formattedS).reverse().toString();
        if (reversed.equals(formattedS)){
            return true;
        }
        else{
            return false;
        }     
    }
    // Problem description: https://leetcode.com/problems/valid-palindrome/description/
}