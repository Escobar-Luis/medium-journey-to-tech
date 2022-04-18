# We have a message to decode. Letters are encoded to digits by its position in the alphabet
# Given a non-empty string of digits, how many ways are there to decode it?

def decode_ways(digits):
    # use numbers 1 to 26 to represent all alphabet letters
    prefixes = [str(i) for i in range(1, 27)]

    def dfs(i):
        # we return 1 if our index length are equal to length of digits given
        if i == len(digits):
            return 1
        # Ways to decode a string
        ways = 0
        # remaining digits after every iteration
        remaining = digits[i:]
        # for every prefix from array of prefixes we just made
        for prefix in prefixes:
            # if our remaing digits contain prefix
            if remaining.startswith(prefix):
                # then we add it to our ways by recurively calling the function and finding if we can find another way
                ways += dfs(i + len(prefix)) # add number of ways returned from child node
        # at end of recursive call, we return the number of ways to decode the digits
        return ways

    return dfs(0)

def decode_ways_memo(digits):
    prefixes = [str(i) for i in range(1, 27)]
    # def dfs(i): Recursive, function now takes a second parameter being the memo
    def dfs(i, memo):
        # if we stored this index in our memo
        if i in memo:
            # return that number of ways for specific index
            return memo[i]
        # if i is equal to length of digits, then return 1
        if i == len(digits):
            return 1
        # Initialize ways as 0
        ways = 0
        # Remaining digits are going to be everything after index
        remaining = digits[i:]
        # for every prefix in our prefixes
        for prefix in prefixes:
            # if the remaining digits start with one of our prefixes
            if remaining.startswith(prefix):
                # ways += dfs(i + len(prefix)) The recurive function thus changes to include memo
                ways += dfs(i + len(prefix), memo)
        memo[i] = ways
        return ways
    # return dfs(0) Instead of intializing memo, we pass the hash directly to function
    return dfs(0, {})