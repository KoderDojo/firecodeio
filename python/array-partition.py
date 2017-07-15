"""
Given a sorted list of integers, find partitions such that
each partition denotes a range of consecutive integers.

Note: The input list consists of sorted integers, without
duplicates. Range(a,b) should be denoted as a-b where a
and b are included in the range.

Example:
    Input : [1,2,3,6,7,8,10,11]
    Output : [1-3, 6-8, 10-11]
"""


class Range:
    def __init__(self, a, b):
        self.lo = a
        self.hi = b

    def __repr__(self):
        return f'{self.lo}-{self.hi}'


def find_partitions(input_list):
    if input_list is None or len(input_list) < 2:
        return input_list

    output_list = []

    begin_range = input_list[0]
    current_val = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] == 1 + current_val:
            current_val += 1
            continue

        if begin_range == current_val:
            output_list.append(current_val)
        else:
            output_list.append(Range(begin_range, current_val))

        begin_range = input_list[i]
        current_val = input_list[i]

    if begin_range == current_val:
        output_list.append(current_val)
    else:
        output_list.append(Range(begin_range, current_val))

    return output_list
