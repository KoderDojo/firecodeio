"""
Write a method to determine whether a postive number is Happy.

A number is Happy (Yes, it is a thing!) if it follows a sequence
that ends in 1 after following the steps given below :

Beginning with the number itself, replace it by the sum of the
squares of its digits until either the number becomes 1 or loops
endlessly in a cycle that does not include 1.

For instance, 19 is a happy number.
   Sequence:

      12 + 92 = 82

      82 + 22 = 68

      62 + 82 = 100

      12 + 02 + 02 = 1
"""

from functools import reduce


def sum_of_squares(n):
    n_str = str(n)
    # return sum([int(d)**2 for d in str(number)])
    return reduce(lambda x, y: x + pow(int(y), 2), n_str, 0)


def is_happy_number(number):
    number = abs(number)

    previous_numbers = set()

    while number not in previous_numbers:
        previous_numbers.add(number)
        number = sum_of_squares(number)
        if number == 1:
            return True

    return False
