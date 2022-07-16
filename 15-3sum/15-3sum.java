class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        
        Arrays.sort(nums);
        for(int i = 0; i<nums.length;i++){
            if (i >0 && nums[i] == nums[i-1]){
                continue;
            }
            int l = i+1;
            int r = nums.length -1;
            while (l<r){
                int sum = nums[l] + nums[r] + nums[i];
                if (sum <0){
                    l++;
                }
                else if (sum>0){
                    r--;
                }
                else {
                    int[] toAdd = {nums[i],nums[l],nums[r]};
                    List<Integer> list = Arrays.stream(toAdd).boxed().collect(Collectors.toList());
                    res.add(list);
                    l++;
                    while (nums[l] == nums[l-1] && l<r){
                        l++;
                    }
                }
                
            }
        }
        return res;
    }
}