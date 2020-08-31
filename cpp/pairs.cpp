class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int pairs = 0;
        for (int i = 0; i < nums.size() - 1 ; i++){
            for (int j = i + 1; j < nums.size(); j++){

                pairs += nums[i] == nums[j];
            }
        }
        return pairs;
    }
};