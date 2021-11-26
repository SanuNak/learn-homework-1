"""
Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    products_sold = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

    def summa_and_averige_sold(products_sold: list):
        '''
        Метод для расчета
        - суммы продаж каждой модели за месяц
        - среднее количество продаж в месяц
        - суммарного количество продаж всех моделей за год
        - Среднего количество продаж всех моделей
        '''
        sold_summa_and_avg = []
        avg_sold_manth = []
        year_solds = []

        for product in products_sold:
            sold_summa_and_avg.append(f'модель: {product["product"]}, '
                         f'прод в год: {sum(product["items_sold"])}, '
                         f'средн прод в месяц: {int(sum(product["items_sold"])/12)}')

            year_solds += product["items_sold"]

        summa_year_solds = f'Продажи за год всех позиций {sum(year_solds)}'
        avg_year_solds = f'Средн кол-во продаж за год всех позиций {int(sum(year_solds)/12)}'
        return sold_summa_and_avg, summa_year_solds, avg_year_solds

    def printing_info(printing_parametrs):
        '''
        Метод для вывода на экран результата
        '''
        for parametr in printing_parametrs:
            # Если результат список, то список пропускаем еще через один цикл, если не список то сразу выводим
            if isinstance(parametr, list):
                for unit in parametr:
                    print(unit)
            else:
                print(parametr)

    printing_info(summa_and_averige_sold(products_sold))

if __name__ == "__main__":
    main()
