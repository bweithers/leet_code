class Solution {
public:
    int numRabbits(vector<int>& answers) {
        if (answers.empty()) return 0;
        vector<int> bookkeeping(1000,0);
        int retval = 0;
        for(int i = 0; i < answers.size(); i++){
            bookkeeping[answers[i]]++;
            if (bookkeeping[answers[i]] == answers[i]+1) {
                retval += answers[i] + 1;
                bookkeeping[answers[i]] = 0;
            }
        }
        for (int i = 0; i < bookkeeping.size(); i++){
            if (bookkeeping[i]) retval += i + 1;
        }
        return retval;
    }
};