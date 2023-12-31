# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.
# test.assert_equals(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")

def get_count(sentence):
    return len([letter for letter in sentence if letter.lower() in 'aeiouy'])
    # return sum(x in 'aeiou' for x in sentence)

print(get_count("aeiouy"))