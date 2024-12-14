"""
Determine sameness or sub-listyness
"""

SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif any(
        list_one == list_two[i : i + len(list_one)]
        for i in range(len(list_two) - len(list_one) + 1)
    ):
        return SUBLIST
    elif any(
        list_two == list_one[i : i + len(list_two)]
        for i in range(len(list_one) - len(list_two) + 1)
    ):
        return SUPERLIST
    else:
        return UNEQUAL


# print(sublist(list_one, list_two))
