class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character,Integer> counts = new HashMap<>();
        int longest = 0;
        int l = 0;
        int maxFreq = 0;
        for(int r =0; r<s.length();r++){
            // if (counts.containsKey(s.charAt(r))){
            //     counts.put(counts.get(s.charAt(r)) +1)
            // }
            counts.put(s.charAt(r), counts.containsKey(s.charAt(r)) ? counts.get(s.charAt(r)) + 1 : 1);
            maxFreq = Math.max(maxFreq, counts.get(s.charAt(r)));
            
            while (r-l+1 - maxFreq >k){
                counts.put(s.charAt(l), counts.get(s.charAt(l)) - 1);
                l++;
            }
            longest = Math.max(longest, r-l+1);
        }
        return longest;
    }
}