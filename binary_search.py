"""
Binary search through a list 
to find the index of a given value
"""

def find(search_list, value, start_index=0):
    if not search_list or value < min(search_list) or value > max(search_list):
        raise ValueError("value not in array")
    mid = len(search_list) // 2
    if search_list[mid] == value:
        return start_index + mid
    elif value > search_list[mid]:
        return find(search_list[mid + 1 :], value, start_index + mid + 1)
    else:
        return find(search_list[:mid], value, start_index)


find([1, 3, 4, 6, 8, 9, 11], 8)
