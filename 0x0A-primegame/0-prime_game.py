#!/usr/bin/python3
""" Prime game
"""


def sieve_of_eratosthenes(max_num):
    """find all primes up to max_number"""
    prime = [True for i in range(max_num + 1)]
    prime[0] = prime[1] = False
    p = 2

    while (p * p <= max_num):
        if prime[p]:
            for i in range(p * p, max_num + 1, p):
                prime[i] = False
        p += 1
    return prime


def isWinner(x, nums):
    """ Prime game
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    prime = sieve_of_eratosthenes(max_num)

    prime_count = [0 for i in range(max_num + 1)]
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
