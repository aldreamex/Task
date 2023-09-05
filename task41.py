# В этом небольшом задании вам дается строка чисел, разделенных пробелами,
# и вы должны вернуть наибольшее и наименьшее число.
#
# Примеры
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Примечания
# Все номера действительны, нет необходимости их проверять.Int32
# Во входной строке всегда будет хотя бы одно число.
# Выходная строка должна состоять из двух чисел, разделенных одним пробелом, а наибольшее число должно быть первым.
def high_and_low(numbers):
    lst = numbers.split(' ')
    lst1 = []
    for item in lst:
        lst1.append(int(item))
    lst1.sort()
    max = str(lst1[-1])
    min = str(lst1[0])
    return max + ' ' + min

    # def high_and_low(numbers):
    #     lst = numbers.split(' ')
    #     lst1 = []
    #     for item in lst:
    #         lst1.append(int(item))
    #     maxim = max(lst1)
    #     minim = min(lst1)
    #     return str(maxim) + ' ' + str(minim)

    return minstr

print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))
