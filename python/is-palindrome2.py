"""
Write a function that takes in a string and returns
a Boolean -> True if the input string is a palindrome
and False if it is not. An empty string is considered
a palindrome. You also need to account for the space
character. For example, "race car" should return False
as read backward it is "rac ecar".
"""


def is_palindrome(input_string):
    """
    Checks if a string is a palindrome.

    :param input_string: str, any string
    :return: boolean, True if palindrome else False

    >>> is_palindrome("madam")
    True
    >>> is_palindrome("aabb")
    False
    >>> is_palindrome("race car")
    False
    >>> is_palindrome("")
    True
    """
    if input_string is None or len(input_string) == 0:
        return True

    if input_string[0] != input_string[-1]:
        return False

    return is_palindrome(input_string[1:-1])
