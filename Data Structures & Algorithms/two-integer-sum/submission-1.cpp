class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>index;
        for (int i=0;i<nums.size();i++){
            int search=target-nums[i];
            if (index.find(search)!=index.end()){
                return {index[search],i};
            }
            index[nums[i]]=i;
        }
    }
};
