#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s
    triangle of n"""

    pascal_list = []

    if n > 0:

        for i in range(n):
            if i == 0:
                pascal_list = [[1]]
            else:
                current_row = [1]
                previous_row = pascal_list[i - 1]
                for j in range(len(previous_row) - 1):
                    current_row.append(previous_row[j] + previous_row[j + 1])

                current_row.append(1)
                pascal_list.append(current_row)

    return pascal_list
