# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# patrick feeney => P.F

def abbrev_name(name):
    list_name = name.split(' ')
    list_name_1 = list_name[0][0].upper()
    list_name_2 = list_name[1][0].upper()
    return str(list_name_1 + '.' + list_name_2)

print(abbrev_name("Evan C"))
