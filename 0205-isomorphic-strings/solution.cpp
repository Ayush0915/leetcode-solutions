class Solution {
public:
    bool isIsomorphic(string s, string t) {
        
        if(s.size()!=t.size()) return false;

        unordered_map<char,char>mppst;
        unordered_map<char,char>mppts;

        for(int i = 0;i<s.size();i++)
        {
            char a = s[i];
            char b = t[i];
            if(mppst.count(a) && mppst[a]!=b) return false;
            if(mppts.count(b) && mppts[b]!=a) return false;
            mppst[a] =b;
            mppts[b] =a ;
        }

        return true;
        
    }
};
