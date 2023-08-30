# Complete the method that takes a boolean value
# and return a "Yes" string for true,
# or a "No" string for false.
#         test.assert_equals(bool_to_word(True), 'Yes')
#         test.assert_equals(bool_to_word(False), 'No')

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'

    # return "Yes" if boolean else "No"

print(bool_to_word(False))

