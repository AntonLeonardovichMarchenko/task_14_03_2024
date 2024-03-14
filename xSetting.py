# модуль выбора функции сканирования (метод parse)

import doIt

class xSet:

    option = ''

    def __init__(self):
        xSet.option = ''

    def getCmd(self):

        print('cmdOption: ')
        xSet.option = input()
        print(xSet.option)
        self.parse()

    def parse(self):

        # выбор функций для парсинга сайта
        if xSet.option == '1':
            doIt.Proc_1()
        # парсинг сайта, работа с тегами, запись в и чтение из файла test_1.csv
        elif xSet.option == '2':
            doIt.Proc_2()

        # Манипуляция тегами через BeautifulSoup
        elif xSet.option == '3':
            doIt.Proc_3()

        # Обход дочерних элементов.
        # С помощью атрибута children получение дочерних НЕИМЕНОВАННЫХ элементов тега.
        elif xSet.option == '4':
            doIt.Proc_4()


        # all descendants of a tag (children of all its levels)
        elif xSet.option == '5':
            doIt.Proc_5()

        # 'красиво' структурированный HTML код
        elif xSet.option == '6':
            doIt.Proc_6()

        # Поиск HTML - элементов по ID: с помощью метода find можно находить
        # элементы HTML по различным признакам, включая id HTML элемента.
        elif xSet.option == '7':
            doIt.Proc_7()

        # Поиск всех HTML-элементов по названию.
        # Здесь поиск проводится по элементу li
        elif xSet.option == '8':
            doIt.Proc_8()

        # Здесь организуется поиск всех HTML-элементов, содержащих фрагменты текста,
        # соответствующие регулярным выражениям
        elif xSet.option == '9':
            doIt.Proc_9()

        # форматирование страниц HTML документа. Контроль над выводом
        elif xSet.option == '10':
            doIt.Proc_10()

        # преобразование человекочитаемого (!!!) текста (текст документа или тег),
        # единственную строку Unicode
        elif xSet.option == '11':
            doIt.Proc_11()

    def clear(self):
        xSet.option = ''

# ========================================================================
def DoCommand(xs):
    xs.getCmd()
    xs.clear()

if __name__ == '__main__':

    xs = xSet()
    DoCommand(xs)

