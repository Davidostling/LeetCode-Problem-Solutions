class Solution
{
public:
    int singleNumber(std::vector<int> &nums)
    {
        for (int element : nums)
        {
            if (std::count(nums.begin(), nums.end(), element) == 1)
            {
                return element;
            }
        }
        return -1;
    }
    // Problem description: https://leetcode.com/problems/single-number/description/
};