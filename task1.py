def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'

    summa = 0
    for i in range(n, m, n):
        summa += i
    return summa

print(sum_mul(1, 10))