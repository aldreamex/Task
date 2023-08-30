# Если мы перечислим все натуральные числа ниже 10, кратные 3 или 5, мы получим 3, 5, 6 и 9. Сумма этих кратных равна 23.
#
# Завершите решение так, чтобы оно вернуло сумму всех кратных 3 или 5 ниже переданного числа.
#
# Кроме того, если число отрицательное, верните 0.
#
# Заметка: Если число кратно как 3, так и 5, подсчитайте его только один раз.
# test.assert_equals(solution(4), 3)
# test.assert_equals(solution(6), 8)

def solution(number):
    summa = 0
    for i in range(0, number):
        if ((i % 3 == 0) or (i % 5 == 0)):
            summa += i
    return summa

# return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution(6))
