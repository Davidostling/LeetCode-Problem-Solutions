class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] inputArr = pattern.split("(?!^)");
        String[] patternArr = s.split(" ");

        Map<String, String> map = new HashMap<String, String>();

        for (int i = 0; i <= inputArr.length - 1; i++) {
            if (map.get(inputArr[i]) == null) {
                map.put(inputArr[i], patternArr[i]);
            }

        }

        String patternChecker = "";
        for (int i = 0; i <= inputArr.length - 1; i++) {
            patternChecker += map.get(inputArr[i]) + " ";
        }

        if (patternChecker.trim().equals(s) && (!map.get("a").equals(map.get("b")))) {
            return true;
        } else {
            return false;
        }
    }
    // Problem description: https://leetcode.com/problems/word-pattern/
}