# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# test.assert_equals(square_sum([1, 2]), 5)
# test.assert_equals(square_sum([0, 3, 4, 5]), 50)
# test.assert_equals(square_sum([]), 0)

def square_sum(numbers):
    res = 0
    for i in numbers:
        res = res + i * i
    return res
  # return sum(x * x for x in numbers)

print(square_sum([1,2]))