from test_framework import generic_test
import math


# Given n, return all primes up to and including n.
# def generate_primes(n):
#     primes = []
#     for i in range(2, n+1):
#         is_prime = True
#         for k in range(int(math.floor(math.sqrt(i))), 1, -1):
#             if i % k == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(i)
#     return primes


def generate_primes(n):
    is_prime = [True] * (n+1)
    for k in range(2, n):
        for j in range(2, n // k + 1):
            is_prime[k * j] = False
    primes = []
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            primes.append(i)
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
