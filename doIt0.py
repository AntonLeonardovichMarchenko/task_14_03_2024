# это полигон для обкатки методов BeautifulSoup на html файле originBS.html
# Импорт класса BeautifulSoup из модуля bs4.
# BeautifulSoup — это основной класс для выполнения
# парсинга по HTML документу. ============================================
from bs4 import BeautifulSoup

# Открытие файла originBS.html. Чтение его содержимого с помощью метода read().
with open('originBS.html', 'r') as f:
    # html-данные присваиваются переменной contents
    contents = f.read()

    # Создается объект-представитель BeautifulSoup. HTML-данные из contents, прочитанные
    # из originBS.html, передаются конструктору. Второй параметр конструктора определяет
    # синтаксический анализатор.
    soup = BeautifulSoup(contents, 'lxml')

    # Здесь выводится HTML-код двух тегов: <head> и <h2>.
    # заголовки
    print(soup.head)
    print(soup.h2)

    # Также в originBS.html имеется несколько элементов <li> и это вывод
    # первого из них.
    print(soup.li)

    # Таким образом, в самом простом случае парсинг сводится к созданию объекта-парсера.
    # Всё остальное происходит само собой.
    # ====================================================================

    # Манипуляция тегами через BeautifulSoup
    # Атрибут name тега дает его название, а атрибут text — его текстовое содержание.

    #from bs4 import BeautifulSoup
    print('Tag manipulation via BeautifulSoup')
    # Открытие HTML файла для чтения.
    with open('originBS.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        print(f'HTML: {soup.h2}, имя: {soup.h2.name}, содержимое: {soup.h2.text}')

        print(f'HTML: {soup.ul}, имя: {soup.ul.li}, содержимое: {soup.ul.li.text}')

    # ====================================================================
    # Практически то же самое применение BeautifulSoup:
    # BeautifulSoup теги, атрибуты name и text.
    # Атрибут name указывает на название тега, а
    # атрибут text указывает на его содержимое.
    # Далее в примере вывод HTML-кода, названия и текста h2 тега. ========

    #from bs4 import BeautifulSoup

    with open("originBS.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        print("HTML: {0}, name: {1}, text: {2}".format(soup.h2,         # тег целиком
                                                       soup.h2.name,    # название тега
                                                       soup.h2.text))   # содержимое тега

#   BeautifulSoap: перебор HTML тегов ====================================
# Метод recursiveChildGenerator() позволяет перебрать содержимое HTML-документа.

# Перебор содержимого HTML-документа и вывод названий ВСЕХ его тегов.
print('Iterate through the contents of an HTML document and display the names of ALL its tags')

#from bs4 import BeautifulSoup

with open("originBS.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    # Данные теги являются частью рассматриваемого HTML-документа.
    for child in soup.recursiveChildGenerator():
        if child.name:
            print(child.name)

#
#   Красивое структурирование HTML кода ==================================
# С помощью метода prettify можно структурировать исходный (soup) HTML-код .

print('go prettify:')

#from bs4 import BeautifulSoup
with open("originBS.html", "r") as f:
    contents = f.read()

    # soup - это ОБЪЕКТ сложной структуры. Он формируется из contents
    # Там много всего наворочено! в том числе, HTML код страницы.
    # так вот, сначала определяется этот самый объект...
    soup = BeautifulSoup(contents, 'lxml')

    # ...а затем к нему применяется метод prettify()
    pr = soup.prettify()

# в результате получается  'красиво' структурированный HTML код
# и его красота состоит в том, что он БЕЗ ЛИШНИХ НАВОРОТОВ просто
# извлекается из soup!
print(pr)

print('===== prettify ====================================================')

# ========================================================================
# BeautifulSoup атрибут children. При помощи атрибута children можно вывести
# все дочерние теги. Здесь извлекаются дочерние элементы html тега, после чего
# они помещаются в список Python и выводятся в консоль.

#from bs4 import BeautifulSoup

with open("originBS.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    root = soup.html   # получился тег html. И у него действительно ДВА дочерних тега
    root_childs = [e.name for e in root.children if e.name is not None]
    # Атрибут children также убирает пробелы между тегами. Поэтому необходимо
    # добавить условие, которое позволяет выбирать только названия тегов.
    print(root_childs)

#   BeautifulSoup атрибут descendants ====================================
# Атрибут descendants позволяет получить список ВСЕХ потомков
# (дочерних элементов всех уровней) рассматриваемого тега.
# Здесь находятся ВСЕ потомки главного тега body.

#from bs4 import BeautifulSoup

with open("originBS.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    root = soup.body
    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)
# ========================================================================
with open("originBS.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    root = soup.body
    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)

# ========================================================================
# С помощью метода recursiveChildGenerator обходится HTML-документ.
# результат (имена тегов) пишутся в htmlElements =========================
print('========== recursiveChildGenerator: all tags in HTML ==========')
#from bs4 import BeautifulSoup

htmlElements = list()
with open('originBS.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    for child in soup.recursiveChildGenerator():
        if child.name:
            print(child.name)
            htmlElements.append(child.name)

    print(htmlElements)

print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
# Обход дочерних элементов
# С помощью атрибута children можно получить дочерние ИМЕНОВАННЫЕ элементы тега.

#from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:
     contents = f.read()
     soup = BeautifulSoup(contents, 'lxml')
     root = soup.html
     # тернарным оператором собираются все дочерние именованные элементы
     root_childs = [e.name for e in root.children if e.name is not None]
     print(root_childs)

# Обход потомков элемента
# С помощью атрибута descendants получают всех потомков (детей всех уровней) тега.
print("Traversing an element's descendants")
from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:
     contents = f.read()
     soup = BeautifulSoup(contents, 'lxml')
     root = soup.body
     root_childs = [e.name for e in root.descendants if e.name is not None]
     print(root_childs)
# Извлекаются все потомки тега <body>.

#   Поиск HTML - элементов по ID =========================================
# С помощью метода find можно находить элементы HTML по различным признакам,
# включая id HTML элемента.

#from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    print(
        soup.find('ul', {'id': 'mylist'})
    )

# пример кода для поиска тега ul, который имеет id mylist.

# Поиск всех HTML-элементов по названию ==================================
# С помощью метода find_all находятся все элементы, которые соответствуют
# некоторым критериям.

#from bs4 import BeautifulSoup

print('========== find_all ==========')


with open('originBS.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
# это было создание объекта soup =========================================

    # а теперь из множества html объектов в soup вытащить ВСЕ объекты с
    # именем тега 'li' и из этого множества объектов извлечь информацию,
    # которую они там содержат - это значение атрибута text.
    for tag in soup.find_all('li'):
        print(f'{tag.name}: {tag.text}')

# ========================================================================
# Метод find_all может принимать список с названиями элементов для поиска.

#from bs4 import BeautifulSoup

tagList = ['h2', 'p'] # список с названиями HTML элементов для поиска

with open('originBS.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # ВЫБОРОЧНОЕ применение метода find_all, результат преобразуется в список элементов
    tags = soup.find_all(tagList)

    # список элементов разбивается на отдельные описания. Описания преобразуются в строки
    # без символов перевода со стоки на строку '\n'
    for tag in tags:
        print(' '.join(tag.text.split()))

    # ====================================================================

    # и при этом генератор списка с условием ПРОЩЕ оператора цикла с условием?
    # Возможно,что компактнее (в одну строку), но точно не проще для понимания!
    # tgList = list()
    # for tag in tags:
    #       if ' '.join(tag.text.split()):
    #           tgList.append(' '.join(tag.text.split()))


    tgList = [' '.join(tag.text.split()) for tag in tags  if ' '.join(tag.text.split())]
    #                                                     условие включения в список
    #                                    какого элемента списка и ОТКУДА
    #        что, собственно включать! Это преобразованный tag из tags (ДВА оператора преобразования -
    #        один непосредственное преобразование, второй - условие включения)

    i = 0
    for tag in tgList:
        print(f'{i}: {tag}')
        i+=1


# Метод find_all в качестве параметра также может принимать ФУНКЦИЮ,
# которая определяет, какие HTML элементы должны быть возвращены.

# Эта функция выбирает пустые HTML элементы, заданные параметром tag.
def emptyFun(tag):
    return tag.is_empty_element

#from bs4 import BeautifulSoup


with open('originBS.html', 'r') as f:

    # объект soup с информацией из originBS.html
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # найти функцией emptyFun ВСЕ пустые элементы.
    # Единственным пустым элементом в документе является <meta>.
    tags = soup.find_all(emptyFun)
    print(tags)

    # Также можно организовать поиск HTML элементов с помощью метода soup.find_all
    # и регулярных выражений в качестве аргументов.

    import re   # подгружается модуль для работы с регулярными выражениями
    #from bs4 import BeautifulSoup

    with open('originBS.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')      # объект soup

        #  получение списка строк, которые содержат подстроку 'BSD'
        strings = soup.find_all(string=re.compile('BSD'))

        # Вывод найденных строк (HTML элементов), содержащих подстроку BSD.
        for txt in strings:
            print(' '.join(txt.split()))

# BeautifulSoup и селекторы. Поиск HTML-элементов по CSS-селектору. ======
# Подробнее про CSS-селекторы - в description.txt. С помощью методов select
# и select_one можно применять некоторые селекторы CSS для поиска
# HTML-элементов. ========================================================

#from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    res = soup.select('li:nth-of-type(3)')
    # В примере используется CSS селектор для поиска и вывода HTML кода третьего элемента <li>.
    print(res)

# [<li>Debian</li>]
# Это третий элемент <li>.


# В примере выводится МОДИФИЦИРОВАННЫЙ элемент, имеющий идентификатор mylist.
# Это <ul... и все вложенные <li... Служебные теги и символы перехода на
# новую строку удалены.
#from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # HTML-элемент по тегу "mylist" успешно находится. И здесь имеет место быть
    # одна тонкость... В этом поисковом контексте символ # используется в CSS для
    # указания (выбора) тегов по их id-атрибутам.
    print(
        soup.select_one('#mylist')
    )

    # Символ # используется в CSS для выбора тегов по их id-атрибутам!
    resSelect = str(soup.select_one('#mylist'))
    resSelect = resSelect.replace('<ul','')
    resSelect = resSelect.replace('</ul', '')
    resSelect = resSelect.replace('<li>', '')
    resSelect = resSelect.replace('</li>', '')
    resSelect = resSelect.replace('>', '')

    resSelect = resSelect.split('\n')
    # соответствующий тег найден по CSS селектору и преобразован к списку ПОДСТРОК!
    resSelect = resSelect[1:len(resSelect)-1:1]
    # первая подстрока - собственно ul и последняя - пустая из списка удалены

    i=0
    for rs in resSelect:
        print(f"{i}... {rs}"
        )
        i+=1


# Создание и добавление тега в тело другого тега: Метод append добавляет новый тег в HTML-документ.

#from bs4 import BeautifulSoup
with open('originBS.html', 'r') as f:

    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # soup с помощью метода new_tag создаёт новый тег li
    newtag = soup.new_tag('li')
    # значение тега - 'OpenBSD'
    newtag.string = 'OpenBSD'

    # это внешний тег - ссылка на тег <ul>
    ultag = soup.ul
    # и туда добавляется только что созданный тег <li>OpenBSD</li>
    ultag.append(newtag)

    print('append **********')
    print(
        ultag.prettify()
    )



# Метод insert вставляет тег в заданное место.
# Вставка тега в определенном месте ======================================

#from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:

    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml') # объект soup

    newtag = soup.new_tag('li')
    newtag.string = 'OpenBSD'   # новый тег <li> 'OpenBSD' </li>

    ultag = soup.ul
    ultag.insert(2, newtag)     # место вставки нового тега

# В этом примере созданный тег <li> вставляется на третью позицию в тело тега <ul>.
    print('insert @@@@@@@@@@')
    print(
        ultag.prettify()
    )

# Замена текста в HTML элементе ==========================================
# Метод replace_with заменяет текст внутри элемента.
#
#from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:

    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # В этом примере конкретный элемент найден с помощью метода find,
    # а его содержимое заменено с помощью метода replace_with.

    tag = soup.find(string='Windows')
    tag.replace_with('OpenBSD')


    print('^^^^^^^^^^ replace_with ^^^^^^^^^^')
    print(
        soup.ul.prettify()
    )

# Удаление HTML элемента =================================================
# Метод decompose удаляет тег из HTML-документа и УНИЧТОЖАЕТ его.

#from bs4 import BeautifulSoup

with open('originBS.html', 'r') as f:

    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # В этом примере удаляется второй элемент <p>.
    ptag2 = soup.select_one('p:nth-of-type(2)')
    ptag2.decompose()

    print('__________ decompose __________')
    print(
        soup.body.prettify()
    )

