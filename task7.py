# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
# test.assert_equals(even_or_odd(2), "Even")
#         test.assert_equals(even_or_odd(1), "Odd")
#         test.assert_equals(even_or_odd(0), "Even")
#         test.assert_equals(even_or_odd(1545452), "Even")
#         test.assert_equals(even_or_odd(7), "Odd")
#         test.assert_equals(even_or_odd(78), "Even")

def even_or_odd(number):
    return 'Even' if number % 2 ==0 else 'Odd'

print(even_or_odd(4))
