import string
prefixes=[str(i) for i in range(1,27)]
print(prefixes)
char = list(string.ascii_uppercase)
print(char)
cyph = dict( zip(char,prefixes) )
print(cyph)

def decode_ways(digits):
    prefixes = [str(i) for i in range(1, 27)]
    def dfs(i, memo):
        if i in memo:
            return memo[i]
        if i == len(digits):
            return 1
        ways = 0
        remaining = digits[i:]
        for prefix in prefixes:
            if remaining.startswith(prefix):
                ways += dfs(i + len(prefix), memo)
        memo[i] = ways
        return ways
    x=dfs(0, {})
    return x

decode_ways('11223')



