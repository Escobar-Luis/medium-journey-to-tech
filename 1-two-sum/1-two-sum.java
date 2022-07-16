class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        
        for (int i = 0; i < nums.length;i++){
            int currentNum = nums[i];
            int need = target - currentNum;
            
            if(seen.containsKey(need)){
                return new int []{seen.get(need),i};
            }
            seen.put(currentNum, i);
        }
        return new int[]{};
    }
    
}