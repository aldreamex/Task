# При наличии массива целых чисел возвращаем новый массив с удвоением каждого значения.
#
# Например:
#
# [1, 2, 3] --> [2, 4, 6]

def maps(a):
    return list(map(lambda x: x*2, a))

# def maps(a):
#     lst = []
#
#     for item in a:
#         lst.append(item*2)
#     return lst

print(maps([1, 2, 3]))