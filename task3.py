# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]

def add_length(str_):
    list= str_.split()

    new_list = []
    for item in list:
        item_length = len(item)
        new_list.append(f'{item} {item_length}')
    return new_list


# def add_length(str_):
#     result_list = [f'{item} {len(item)}' for item in str_.split()]
#     return result_list

print(add_length('Яблоко киви груша машина'))