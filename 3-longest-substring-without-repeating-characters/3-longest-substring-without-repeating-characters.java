class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> inSubString = new HashSet<>();
        
        int l = 0;
        int longest = 0;
        for(int r = 0; r<s.length();r++){
            while (inSubString.contains(s.charAt(r))){
                inSubString.remove(s.charAt(l));
                l++;
            }
            inSubString.add(s.charAt(r));
            longest = Math.max(longest, r-l+1);
        }
        return longest;
    }
}