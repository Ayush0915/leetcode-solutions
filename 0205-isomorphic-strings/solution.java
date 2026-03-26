class Solution {
    public boolean isIsomorphic(String s, String t) {
        for(int i=0;i<s.length();i++)
        {
            for(int j=i;j<s.length();j++)
            {
                if(s.charAt(i)==s.charAt(j)||t.charAt(i)==t.charAt(j))
                {
                    if(t.charAt(i)!=t.charAt(j)||s.charAt(i)!=s.charAt(j))
                    return false;
                }

            }
        }
        return true;
    }
}
