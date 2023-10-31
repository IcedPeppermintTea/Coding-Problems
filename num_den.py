"""
Given two arrays num[] and den[] which denotes the
numerator and denominator respectively, the task is
to find the count of the unique fractions.
"""
from math import gcd

def reduce_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def count_unique_fractions(num, den):
    unique_fractions = set() # list that will contain all the unique fractions
    n = len(num)

    for i in range(n):
        reduced_fraction = reduce_fraction(num[i], den[i])
        unique_fractions.add(reduced_fraction)
    return len(unique_fractions) # return length of unique_fractions


if __name__ == '__main__':
    numerator = [1,2,3,4,5]
    denominator = [2,4,6,1,11]
    result = count_unique_fractions(numerator, denominator)
    print("Count of unique fractions: ", result)
