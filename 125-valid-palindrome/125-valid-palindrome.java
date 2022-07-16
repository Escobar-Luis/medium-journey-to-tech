class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;
        
        while (l<r){
            Character start = s.charAt(l);
            Character end = s.charAt(r);
            
            if (!Character.isLetterOrDigit(start)){
                l++;
            }
            else if(!Character.isLetterOrDigit(end)){
                r--;
            }
            else if (Character.toLowerCase(start) != Character.toLowerCase(end)){
                return false;
            }
            else{
            l++;
            r--;}
            
        }
        return true;
    }
}