class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> retval;
        if (candies.empty()) return retval;
        int max_candies = 0;
        for (int i = 0; i < candies.size(); i++) max_candies = max(max_candies, candies[i]);
        for (int i = 0; i < candies.size(); i++) retval.push_back( (candies[i] + extraCandies) >= max_candies);
        return retval;
    }
};