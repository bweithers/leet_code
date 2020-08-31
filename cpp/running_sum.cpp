class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> retval;
        if (nums.empty()) return retval;
        retval.push_back(nums[0]);
        for (int i = 1; i < nums.size(); i++){
            retval.push_back(retval[i-1] + nums[i]);
        }
        return retval;
    }
};