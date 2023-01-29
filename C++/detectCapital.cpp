class Solution
{
public:
    bool detectCapitalUse(string word)
    {
        int countUpper = count_if(word.begin(), word.end(), ::isupper);
        return countUpper == 0 || countUpper == word.length() || (countUpper == 1 && ::isupper(word[0]));
    }
};
