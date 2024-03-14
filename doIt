# Подключение блиотеки, которая позволяет работать с HTML- и XML-кодом.
##from bs4 import BeautifulSoup

# Библиотека requests. Помогает сделать запрос на нужный адрес сайта.
##import requests

# Проверка работы библиотек. =============================================
# Сохраняется в переменную URL-адрес страницы, с которой планируется парсить
# информацию:
##url = 'https://geophys.geol.msu.ru/'

# К ней создаётся запрос.
##page = requests.get(url)

#  Распечатка результатов работы сервера. Ответ '200'  означает,
#  что библиотека requests работает правильно и сервер отдаёт информацию со страницы.
##print(page)

# Теперь используется библиотека Beautiful Soup. С её помощью со страницы получается
# ВЕСЬ исходный код. Тут всё просто. Важно правильно спросить. Про всё в общем спросили
# - ПРО ВСЁ ответ и получили!
##soup = BeautifulSoup(page.text, "html.parser")

# результат выводится на экран.
##print(soup)

# BeautifulSoup и веб-скрапинг HTML ======================================
# Requests является HTTP библиотекой в Python. Она позволяет использовать РАЗНООБРАЗНЫЕ
# методы для получения доступа к веб-ресурсам при помощи HTTP. Надо только понимать как применить!



from bs4 import BeautifulSoup
import requests as req

import xCsvReadWrite as crw
#import xSetting as set

# import csv   # здесь не нужен. Объявлен в модуле xCsvReadWrite

# ========================================================================
#setterProcessor = set.xSet()

# Извлечение названия рассматриваемой веб-страницы.
# Здесь также выводится имя ее родителя.

#setterProcessor.getCmd()

# ========================================================================
def Proc_1():
    csvMaker = crw.xCsvClass('test_1.csv', 'w')  # объект для обслуживания csv на запись
    url = "https://geophys.geol.msu.ru"    # url страницы
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')    # объект soup для веб-страницы

    print('>>>>>>>>>>>>>>>>>>>>>> soup.title')
    print(soup.title)
    csvMaker.valueToDatas([0,'soup.title',soup.title])
    csvMaker.valueToDatas(soup.title)

    csvMaker.valueToDatas([])

    print('>>>>>>>>>>>>>>>>>>>>>> soup.title.text')
    print(soup.title.text)
    csvMaker.valueToDatas([1,' soup.title.text ',soup.title.text])
    csvMaker.valueToDatas([soup.title.text])

    csvMaker.dataProcess()


    print('>>>>>>>>>>>>>>>>>>>>>> soup.title.parent')
    # а родителем для всего этого хозяйства, ограниченного тегами <title> и </title> и
    # собственно представляющего строку - "имя тега" .text, является фрагмент страницы,
    # ограниченный тегами <head> и </head>. Туда же входит и код между тегами <title> и </title>
    print(soup.title.parent)

    csvMaker._close()

    print('>>>>>>>>>> soup.script, soup.script.name .....')
    print(soup.script)
    print(soup.script.name)
    print('>>>>>>>>>> soup.iframe.....')
    print(soup.iframe)
    print('>>>>>>>>>> soup.footer.....')
    print(soup.footer)
    print(soup.footer.li)
# ========================================================================

    csvMaker = crw.xCsvClass('test_1.csv', 'r')  # объект для обслуживания csv на чтение
    print('_______________________________________________________________')

    csvMaker.dataProcess()
    csvMaker.printAll()
    csvMaker._close()

    print('---------------------------------------------------------------')

# ========================================================================

# ========================================================================
def strNorm(strParam):

    strRet=''

    strLen = len(strParam)

    for l in range(strLen):
        if strParam[l].isupper():
            #strRet = strRet + '\n'
            strRet = strRet + strParam[l]
        elif strParam[l].islower():
            strRet = strRet + strParam[l]
        elif strParam[l] == ' ':
            strRet = strRet + strParam[l]

    #strRet = ',' + strRet  # !!!!!!!!!!
    return strRet


def Proc_2():
#   BeautifulSoap: перебор HTML тегов ====================================
# Метод recursiveChildGenerator() позволяет перебрать содержимое HTML-документа.
# Перебор содержимого HTML-документа и вывод названий ВСЕХ его тегов.
# Эта функция предполагает сканирование сайта Кафедры геофизических методов исследования
# земной коры геологического факультета МГУ, выделение, отбор (тег данного типа входит
# во множество отобранных тегов строго ОДИН раз). Общее количество тегов нумеруется - более 1500.
# Атрибут text отобранного тега подвергается дополнительной обработке на предмет повышения
# его читабельности (strNorm) далее производится запись отобранных атрибутов в .csv файл.
# Запись производится стандартными методами, доступными из модуля csv. На этом этапе результат
# работы данной функции виден в файле test_1.csv.
# Формат записи: <порядковый номер записи, "текст">.
# Текст записывается в том виде, как его "увидели" методы парсинга класса BeautifulSoup.
# Здесь для простоты это файл всегда под одним именем. Разумеется, в реальных боевых
# условиях этот недостаток легко устраняется. Далее с помощью стандартных методов из
# модуля csv производится чтение ранее записанной в test_1.csv информации.
# После небольшой дополнительной обработки (методы класса xCsvClass) результаты работы
# (чтение test_1.csv) выводятся на консоль приложения. Туда выкидывается много всякой
# отладочной информации, но непосредственно прочитанная из test_1.csv наглядно
# выделяется строками разделителя (=====). Сопоставление записанной и прочитанной информации
# демонстрирует их соответствие - от порядкового номера записей, их количества
# (много найденных, да немного записанных!), до их положения на строке записи: на строке
# и в файле какие-либо специфические привязки к местоположению. Есть различие в представлении:
# блокнот (программа, в которой производился просмотр .csv файла обеспечивает масштабитование
# страниц при изменении размеров окна. API python'а таких возможностей не поддерживает).
# А вообще, хорошо бы знать, кто такой САЙТИЩЕ отгрохал! Короче, уважение мастерам веб
# программирования.
# ========================================================================
    import requests as req
    from bs4 import BeautifulSoup
    csvMaker = crw.xCsvClass('test_1.csv', 'w')    # объект для обслуживания csv на запись
    htmlElements = list()
    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
    soup = BeautifulSoup(rText, 'lxml')
# Данные теги являются частью рассматриваемого HTML-документа.
    i = 0
    childTxt = ''
    for child in soup.recursiveChildGenerator():
        if child != '\n' and child.name != None:  # а разве может быть пустой или безымянный child тег?
            if child.name not in htmlElements:
                print(f'***** {child.name} *****')
                htmlElements.append(child.name) # список непустых именованных child тегов
                childTxt=' '.join(child.text.split())
                childTxt=strNorm(childTxt)
                if childTxt != '':
                    csvMaker.valueToDatas([f'\n' + str(i)+ ' ' +childTxt]) # !!!!!
            else:
                print(f'----- {child.name} -----')
        i+=1
    print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(htmlElements)     # вывод списка именованных child тегов.
                            # имена всех html тегов
    print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

    # i = 0
    # for tt in soup.title.text:
    #     csvMaker.valueToDatas([f'title.text {i} : ', soup.title.text])
    #     i+=1

    csvMaker.dataProcess()
    csvMaker._close()


    csvMaker = crw.xCsvClass('test_1.csv', 'r')  # объект для обслуживания csv на чтение
    print('_______________________________________________________________')

    csvMaker.dataProcess()
    csvMaker.printAll()
    csvMaker._close()

    print('---------------------------------------------------------------')

# ========================================================================
# далее записи и чтения в csv НЕ производится. Встроенные и построенные
# методы соответствеющих классов действительно обеспечивают запись и чтение
# пропарсерной информации разнообразных форматов, причём разных записей
# на протяжении одного сеанса записи и чтения пропарсенных данных.
# ========================================================================

def Proc_3():
# применение библиотеки BeautifulSoup
# Манипуляция тегами через BeautifulSoup
# Атрибут name тега дает его название, а атрибут text — его текстовое содержание.


    import requests as req
    from bs4 import BeautifulSoup

    print('Tag manipulation via BeautifulSoup')
# Извлечение названия рассматриваемой веб-страницы.

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')     #  soup для  url = 'https://geophys.geol.msu.ru'

    print('---------- soup -----------------------------------------------')
    print(soup)
    print('---------- {soup.h2}, имя: {soup.h2.name}, содержимое: {soup.h2.text} ----------')
    print(f'HTML: {soup.h2}')
    print(f'имя: {soup.h2.name}')
    print(f'содержимое: {soup.h2.text}')
    print('---------------------------------------------------------------')


    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')

def Proc_4():
# применение библиотеки BeautifulSoup
# Обход дочерних элементов
# С помощью атрибута children можно получить дочерние ИМЕНОВАННЫЕ элементы тега.
    print('All child named elements')

    from bs4 import BeautifulSoup

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
    soup = BeautifulSoup(rText, 'lxml')
    root = soup.html
    # тернарным оператором собираются все дочерние неименованные элементы
    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)

# ========================================================================
# применение библиотеки BeautifulSoup
# обеспечивает all descendants of a tag (children of all its levels)
def Proc_5():

    from bs4 import BeautifulSoup
    print('all descendants of a tag (children of all its levels)')
    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
    soup = BeautifulSoup(rText, 'lxml')
    root = soup.html

# тернарным оператором собирают всех потомков (детей всех уровней) тега
    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)

# применение библиотеки BeautifulSoup
# 'красиво' структурированный HTML код
# и его красота заключается в том, что он представляется БЕЗ ЛИШНИХ НАВОРОТОВ
# просто извлекается из soup!
def Proc_6():

    from bs4 import BeautifulSoup
    print('============= soup.prettify: ======================================')

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
    soup = BeautifulSoup(rText, 'lxml')

    pr = soup.prettify()

    # 'красиво' структурированный HTML код как он есть!
    print(pr)


# применение библиотеки BeautifulSoup
# Поиск HTML - элементов по заданным признакам ===========================
# С помощью метода find можно находить элементы HTML по различным признакам,
# включая id HTML элемента.

def Proc_7():

    from bs4 import BeautifulSoup
    print('================ soup.find: =======================================')

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
    soup = BeautifulSoup(rText, 'lxml')
# для url = 'https://geophys.geol.msu.ru' создан объект soup
    found = soup.find('div', {'id': 'site-logo-inner'})
# поиск div ОДНОГО элемента HTML по признаку, задаваемому словарём
# {'id': 'site-logo-inner'}. Вот результат...
    print(found)

# Параметры поиска. Это НАБОР признаков, по которым ведётся поиск . Представляет собой словарь словарей:
# в качестве ключей - имена HTML элементов, в качестве значений
# - СЛОВАРИ с признаками HTML элементов. Таким образом,
# одним оператором (разумеется, с предварительной подготовкой!) удаётся
# получить ВЕСЬ требуемый список элементов HTML
# словарь словарей признаков =============================================
# !!!!! здесь проблема с ключами словаря словарей: теги одного класса (а этих
# классов немного!) для ограниченного количества стандартных атрибутов имеют
# очень большое количество различных значений !!!!!
# Определение параметров поиска

    targets = {
        'div':{'class': "navigation clr"},
        'li' :{'id':"menu-item-335"},
        'ul' :{'class':"menu"},
        'span':{'class':"category"},
        'meta':{'property':"og:site_name"}  # при поиске find меняет местами атрибуты HTML тега
       # тег     атрибут     значение
        }

# непосредственно из словаря словарей список ключей словаря targets ======
    keys = targets.keys()

# для url = 'https://geophys.geol.msu.ru' тернарным оператором с помощью
# метода soup.find формируется список элементов HTML. СЛОВАРИ ПРИЗНАКОВ, по которым
# производится поиск элементов, кодируются выражением targets[_key]
    discovered = [soup.find(_key, targets[_key]) for _key in keys if _key is not None]
# из списка ключей keys выбрать по элементу _key (полный перебор - пока keys не опустеет)
# с очередным ключём-именем HTML и соответствующим значением, задающим признак элемента
# вызвать метод soup.find и сформировать список элементов. Предполагается, что soup
# содержит ВСЮ необходимую информацию, которую остаётся только извлечь методом find.


#print(discovered)
    index = 0
    for _disco in discovered:
        print(f'========================== {index} =========================')
        print(_disco)
        index+=1

    print(f'===================================================')

# применение библиотеки BeautifulSoup
# Поиск всех HTML-элементов по названию ==================================
# С помощью метода find_all находятся все элементы, которые соответствуют
# некоторым критериям.

def Proc_8():
    from bs4 import BeautifulSoup

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
# soup для url = 'https://geophys.geol.msu.ru'
    soup = BeautifulSoup(rText, 'lxml')

# результат применения метода find_all от имени soup к элементам
# li - это МНОЖЕСТВО. Дальнейшие преобразования множества к списку.
    aSet = soup.find_all('li')

# оператор цикла с условием
    tgList = list()
    for a in aSet:
        if ' '.join(a.text.split()):
            tgList.append(' '.join(a.text.split()))

# генератор списка с условием
    tgList = [' '.join(a.text.split()) for a in aSet if ' '.join(a.text.split())]

# Простое преобразование множества в список
    aSet = list(aSet)

# Фильтрация: с применением фильтра к списку aSet, который задаётся функцией
# lambda с одним параметром строится список отфильтрованных li элементов
    result_lst = list(filter(lambda a: a.text != '', aSet))
# фильтруются элементы a списка aSet: в aSet остаются только те элементы, у
# которых атрибут text НЕ является пустой строкой. То есть, a.text != ''.
# Этот фильтрованный список подаётся на вход функции list, которая строит новый
# список фильтрованных элементов.

    n = 0
    for rEl in result_lst:
        print(f'{n}--->: {rEl.text}')
        n+=1

# с применением фильтра к списку aSet, который задаётся функцией lambda с одним
# параметром строится список отфильтрованных li элементов.
# Хорошая новость. Фильтр избавляет от HTML li элементов, связанных с Государственным
# экзаменом: из списка выкидываются ДВА элемента. Маловато будет.
# Надо специально позаниматься с фильтрацией.
    result_lst = list(filter(lambda a: a.text != 'Государственный экзамен', aSet))

    n = 0
    for rEl in result_lst:
        print(f'{n}~~~>:    {rEl.text}')
        n+=1

# ========================================================================
# применение библиотеки BeautifulSoup
# С помощью метода find_all находятся все элементы, которые соответствуют
# некоторым критериям.
# Здесь организуется поиск всех HTML-элементов, содержащих фрагменты текста,
# соответствующие регулярным выражениям ==================================

def Proc_9():

    import re   # модуль для работы с регулярными выражениями

    from bs4 import BeautifulSoup

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
# soup для url = 'https://geophys.geol.msu.ru'
    soup = BeautifulSoup(rText, 'lxml')

#  получение списка строк, которые содержат подстроку 'МГУ'
    strings = soup.find_all(string=re.compile('МГУ'))

# Вывод найденных строк (HTML элементов), содержащих подстроку BSD.
# for txt in strings:
#     print(' '.join(txt.split()))

# генератор списка с условием. Ну очень простой!
# В tgMSU собираются ВСЕ НЕПУСТЫЕ строки из strings
# tgMSU = [string for string in strings if string]

# а такой генератор уже был. Реализуется удаление пробельных символов.
    tgMSU = [' '.join(string.text.split()) for string in strings if ' '.join(string.text.split())]

# это вывод результатов работы генератора на основе списка строк, которые содержат подстроку 'МГУ'
    i = 0
    for str in tgMSU:
        print(f'{i}::: {str}')
        i+=1

# ========================================================================
# применение библиотеки BeautifulSoup
# форматирование страниц HTML документа
# контроль над выводом: можно создать объект одного из классов форматирования
# Beautiful Soup и передать этот объект как formatter
# class bs4.HTMLFormatter
# Используется для задания правил форматирования HTML-документов.
#
#  Преобразование строки в верхний регистр, независимо от того, находится ли строка
#  в текстовом узле - когда текст находится между парными HTML элементами
#  или в значении атрибута - когда строка является фрагментом HTML элемента

# увеличить отступ при красивом форматировании:
# функция форматирования (увеличивает центирование и отступ фрагмента строки на фиксированную величину)
def increasingIndentation(str):
    return f'\n_____{str:^25}...{str:>25}_____\n'
    #          центрирование ... отступ

# функция форматирования (переводит исходную строку в верхний регистр) ===
def uppercase(str):
        return str.upper()
# ========================================================================


def Proc_10():
    from bs4 import BeautifulSoup
    from bs4.formatter import HTMLFormatter

    print('formatter in action! ----------------------------------------------')

# функция форматирования (переводит исходную строку в верхний регистр) ===
# функция uppercase может быть объявлена и как ВЛОЖЕННАЯ! ================
#    def uppercase(str):
#        return str.upper()
# ========================================================================

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
# soup для url = 'https://geophys.geol.msu.ru'
    soup = BeautifulSoup(rText, 'lxml')

# сборка инструмента для форматирования ==================================
# обеспечивает перевод значений атрибутов тегов в верхний регистр

    formatter = HTMLFormatter(uppercase)
# ========================================================================
# область применения форматёра задаётся объектом soup ====================
    print(soup.prettify(formatter=formatter))

    print('=0=')


# сборка инструмента для форматирования ==================================
# обеспечивает центрирование и сдвиг значений атрибутов тегов

    formatter = HTMLFormatter(increasingIndentation)
# ========================================================================
# область применения форматёра задаётся объектом soup ====================
    print(soup.prettify(formatter=formatter))

    print('=1=')

# ========================================================================
# применение библиотеки BeautifulSoup: метод get_text
# Если внутри документа или тега нужен только человекочитаемый (!!!) текст,
# можно использовать метод get_text(). Он возвращает весь текст документа
# или тега в виде единственной строки Unicode:

def Proc_11():
    from bs4 import BeautifulSoup

    print('---------- human readable text ! ----------')

    url = 'https://geophys.geol.msu.ru'
    resp = req.get(url)
    rText = resp.text
# soup для url = 'https://geophys.geol.msu.ru'
    soup = BeautifulSoup(rText, 'lxml')

    strings = soup.get_text('\n', strip=True)    # удалили лишние символы переноса строки
    # вот тот самый soup.get_text... железяка от парсера BeautifulSoup

    strString = strings.split('\n')     # разбили строку по разделителю.
                                        # Фрагменты строки - в списке strString

# Фильтрация: с применением фильтра к списку strString, который задаётся функцией
# lambda с одним параметром строится список отфильтрованных элементов
    result_lst = list(filter(lambda string: string != '' and string != '[...]', strString))
# фильтруются элементы string списка strString: в strString остаются только те элементы,
# которые не являются пустой строкой или последовательностью символов '[...]'.
# Этот фильтрованный список подаётся на вход функции list, которая строит новый список
# фильтрованных элементов.

    i=0
    for string in strString:
        if string != '' and string != '[...]':
            print(f'{i}: {string}') # всё и так получается: список строк, разделённых символами
                                    # переноса строки.
        #print(f'{i}: {" ".join(string.split())}') # а это уже излишняя суета...
        # (разбить на массив подстрок и потом собрать через пробел-разделитель)
            i+=1




