"""
We're sure you've used Microsoft Excel or Google Sheets at some point.
Given a column name of the spreadsheet, return the corresponding column
number. Note: Column name "A" corresponds to column number 1.
"""


def excel_column_name_to_number(column_title):
    if column_title is None or len(column_title) == 0:
        return 0

    column_title = ''.join(reversed(column_title))
    d = {chr(64 + n): n for n in range(1, 27)}

    def letter_to_dec(letters):
        if len(letters) == 1:
            return d[letters]

        return d[letters[-1]] * 26 ** (len(letters) - 1) + letter_to_dec(letters[0:-1])

    return letter_to_dec(column_title)


def excel_column_name_to_number_2(column_title):
    num = 0
    for c in column_title:
        num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num
