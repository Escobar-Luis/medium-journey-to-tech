class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // hashmap where an array representation of 26 ascii letters are key and a list of words is its value
        // Instantiate hashmap, loop trhough strings, for each string instantiate key, for each character in string compute ascii value and update key count at ind, add word as value to key in hash, return hashmap values
        
        HashMap<String, List<String>> map = new HashMap<>();
        
        List<List<String>> res = new ArrayList<>();
        
        for(String word:strs){
            char [] hash = new char[26];
            for(char c :word.toCharArray()){
                hash[c-'a']++;}
            String  key = new String(hash);
            map.computeIfAbsent(key, k -> new ArrayList<>());
            map.get(key).add(word);
            }
        res.addAll(map.values());
        return res;
    }
}