"""
Given a string, recursively compute a new string
where identical, adjacent characters
get separated with a "*".

Example:
insert_star_between_pairs("cac") ==> "cac"

insert_star_between_pairs("cc") ==> "c*c"
"""


def insert_star_between_pairs(a_string):
    if a_string is None or len(a_string) < 2:
        return a_string

    first, second = a_string[0], a_string[1]
    prefix = first + "*" if first == second else first

    return prefix + insert_star_between_pairs(a_string[1:])
