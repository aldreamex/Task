# Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):

    new_list = []

    for index, i in enumerate(my_list):
        if index %2 == 0:
            new_list.append(i)
    return new_list

    # return my_list[::2]

print(remove_every_other(["Keep", "Remove", "Keep", "Remove"]))
