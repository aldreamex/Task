# Ваша задача — сделать функцию, которая может принять в качестве аргумента
# любое неотрицательное целое число и вернуть его с цифрами в порядке убывания.
# По сути, переставьте цифры, чтобы создать максимально возможное число.
# Примеры:
# Вход: 42145 Выход: 54421
# Вход: 145263 Выход: 654321
# Вход: 123456789 Выход: 987654321
# test.assert_equals(descending_order(0), 0)
# test.assert_equals(descending_order(15), 51)
# test.assert_equals(descending_order(123456789), 987654321)

def descending_order(num):
    if num >= 0:
        stroka = str(num)
        lst = list(stroka)
        lst.sort()
        return int(''.join(lst)[::-1])

print(descending_order(123456789))
