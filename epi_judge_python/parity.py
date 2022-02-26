from test_framework import generic_test

# Function that determines the parity of an integer

# Brute-force solution
def parity_brute_force(x: int) -> int:
    result = 0 # assume false
    while x:
        result = result ^ x & 1
        x = x >> 1
    return result

# More efficient solution
def parity(x: int) -> int:
    x = x ^ x >> 32
    x = x ^ x >> 16
    x = x ^ x >> 8
    x = x ^ x >> 4
    x = x ^ x >> 2
    x = x ^ x >> 1
    return x & 1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))