"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def func(string_one, string_two):
        if not isinstance(string_one, str) and not isinstance(string_two, str):
            return 0
        elif not isinstance(string_one, str) or not isinstance(string_two, str):
            return 0
        elif string_one == string_two:
            return 1
        elif string_one != string_two and (len(string_one) > len(string_two)) and string_two != 'learn':
            return 2
        elif string_one != string_two and string_two == 'learn':
            return 3

    print('Выводим результаты выполнения заданий:')
    print('строки одинаковые, результат: ', func('рога', 'рога'))
    print('строки разные и первая длиннее, результат: ', func('копыта', 'рога'))
    print('строки разные и вторая строка "learn", результат: ', func('копыта', 'learn'))

if __name__ == "__main__":
    main()
