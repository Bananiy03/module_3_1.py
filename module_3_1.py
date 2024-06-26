'''
Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.
Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

Пункты задачи:
Создать переменную calls = 0 вне функций.
Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
Создать функцию string_info с параметром string и реализовать логику работы по описанию.
Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).
'''

calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    a = len(string), string.upper(), string.lower()
    print(a)
    return string

def is_contains(string, contains):
    count_calls()
    s_lower = string.lower()
    lst_lower = [item.lower() for item in contains]
    return s_lower in lst_lower


string_info('Capybara')
string_info('Armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))

print(calls)



