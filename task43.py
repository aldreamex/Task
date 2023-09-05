# Вам будет дано слово. Ваша задача состоит в том, чтобы вернуть средний символ слова.
# Если длина слова нечетная, верните средний символ. Если длина слова четная, верните средние 2 символа.
# #Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"
# #Input
# Слово (строка) длины (в javascript вы можете получить чуть больше 1000 в некоторых тестовых примерах из-за ошибки в тестовых примерах).
# Вам не нужно тестировать это. Это только для того, чтобы сказать вам,
# что вам не нужно беспокоиться о том, что время ожидания вашего решения истечет.0 < str < 1000
# #Output
# Средние символы слова, представленные в виде строки.

def get_middle(s):
    if len(s) % 2 == 0:
        sr = len(s) // 2
        simbol = s[sr-1]+s[sr]
        return simbol
    else:
        sr = len(s) // 2
        simbol = s[sr]
        return simbol

print(get_middle("of"))