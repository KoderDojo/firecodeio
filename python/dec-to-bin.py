"""
Binary Representation
Write a function to compute the binary representation of
a positive decimal integer. The method should return a
string.

Example:
dec_to_bin(6) ==> "110"

dec_to_bin(5) ==> "101"

Note : Do not use in-built bin() function.
"""


def dec_to_bin(number):
    """
    Returns the string representation of a binary
    number.

    :param number: int, base 10
    :return: str, string representation base 2

    >>> assert(dec_to_bin(10) == '1010')
    """
    return '{0:b}'.format(number)


def dec_to_bin_recur(number):
    """
    Returns the string representation of a binary
    number.

    :param number: int, base 10
    :return: str, string representation base 2

    >>> assert(dec_to_bin_recur(10) == '1010')
    """
    if number < 2:
        return str(number)

    return dec_to_bin(number // 2) + dec_to_bin(number % 2)
