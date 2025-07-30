class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum1=0,sum2=0;
        int n;
        n=nums.size();
        sum1=(n*(n+1))/2;
        for(int i=0;i<n;i++){
            sum2=sum2+nums[i];
        }
        int missing=sum1-sum2;
        return missing;
    }
};
