# Создайте функцию, которая отвечает на вопрос «Вы играете на банджо?».
# Если ваше имя начинается с буквы «R» или строчной буквы «r», вы играете на банджо!
#
# Функция принимает имя в качестве единственного аргумента и возвращает одну из следующих строк:
#
# name + " plays banjo"
# name + " does not play banjo"
# Приведенные имена всегда являются допустимыми строками.

def are_you_playing_banjo(name):
    if name[0] in 'Rr':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("martin"))
