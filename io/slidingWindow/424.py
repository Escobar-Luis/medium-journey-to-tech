
def characterReplacement_optimized(s: str, k: int) -> int:
    count = {}
    # our result is only going to be maximized when we find a new maxF
    res = 0
    
    l = 0
    maxf = 0
    for r in range(len(s)):
        # add the right pointer char to hash and/or increment it
        count[s[r]] = 1 + count.get(s[r], 0)
        # calculate the maxf instead of having to access all values of hash like in the normal solution
        maxf = max(maxf, count[s[r]])
        # if length of current substring - maxF is greater than allowed changes of k
        if (r - l + 1) - maxf > k:
            # we shift our left pointer and remove one instance of the previous char before the shift from our hash
            count[s[l]] -= 1
            l += 1
        # our res is going to be the max btwn wat we seen, and our current substring
        res = max(res, r - l + 1)
    return res

def characterReplacement_norm(s: str, k: int) -> int:
    # hash to count occurences of each character
    count = {}
    # result is the longest substring we could create with K replacements
    res = 0
    
    l = 0
    for r in range(len(s)):
        # add the right pointer char to hash and/or increment it
        count[s[r]] = 1 + count.get(s[r], 0)
        # make sure current window is valid by asking while it is not valid
        # length of window subtracted from the count of the most frequent character is === to the number of replacements done
        while (r-1+1) - max(count.values())>k:
            count[s[l]] -=1
            l+=1
        # our res is going to be the max btwn wat we seen, and our current window
        res = max(res, r - l + 1)
    return res