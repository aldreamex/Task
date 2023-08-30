# Given an array of integers your solution should find the smallest integer.
#
# For example:
#
# Given your solution will return [34, 15, 88, 2]2
# Given your solution will return [34, -345, -1, 100]-345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int([78, 56, 232, 1, 11, 43]))