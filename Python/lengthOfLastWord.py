class Solution {
    public int lengthOfLastWord(String s) {
        String [] formattedS = s.trim().split(" ");
        int lastWordLength = formattedS[formattedS.length-1].length();
        return lastWordLength;
    }
}

#Problem description https://leetcode.com/problems/length-of-last-word/description/