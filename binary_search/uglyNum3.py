from math import gcd

def nth_ugly_number(n: int, a: int, b: int, c: int) -> int:
    # variables needed to calculate total area of venn diagram i.e count of ugly numbers
    ab = a * b // gcd(a, b)
    bc = b * c // gcd(b, c)
    ac = a * c // gcd(a, c)
    abc = ab * c // gcd(ab, c)
    # Find the # of integers that are divisible by the three numbers (a,b,c) i.e ugly numbers
    def ugly_number_count(k: int) -> int:
        return (k // a + k // b + k // c) - (k // ab + k // bc + k // ac) + k // abc
    min_ptr = n
    max_ptr = n * min(a, b, c)
    boundaryIndex = max_ptr
    while min_ptr <= max_ptr:
        midpoint = (min_ptr + max_ptr) // 2
        if ugly_number_count(midpoint) < n:
            min_ptr = midpoint + 1
        else:
            boundaryIndex = midpoint
            max_ptr = midpoint - 1
            # to prevent integer overflows we take index and modulo it by the guven
    return boundaryIndex % (10 ** 9 + 7)