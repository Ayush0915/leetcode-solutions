class Solution {
public:
    int maxProfit(vector<int>& nums) {
        int i,j;
        int n=nums.size();
        int maxpro=0;
        int minprice=INT_MAX;
        for(i=0;i<n;i++){
            minprice=min(minprice,nums[i]);
            maxpro=max(maxpro,nums[i]-minprice);
            }
    
        return maxpro;
    }
};
