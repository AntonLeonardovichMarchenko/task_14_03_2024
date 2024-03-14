# ======================================================
import csv


# ========================================================================

# а это вообще глобальная функция. И ещё неизвестно, что проще вызывать
# и читать: функцию или метод... =========================================
def DatasClear():
    xCsvClass.Datas.clear()
    xCsvClass.Datas = list()

class xCsvClass:

    Datas = list()
    DataString = ''

    def __init__(self, fName, mode):
        #xCsvClass.Datas = list()
        self.fName = fName
        self.mode = mode
        self.f = open(fName, mode)


    def _close(self):
        self.f.close()

    def dataProcess(self):
        # ================================================================
        if self.mode == 'r':

            DatasClear()

            reader = csv.reader(self.f, delimiter=',',
                                        quotechar=',',
                                        quoting=csv.QUOTE_MINIMAL)


            for row in reader:
                demoStr = ''
                for r in row:
                    demoStr = demoStr + r
                    print(demoStr)

        # ================================================================
        elif self.mode == 'w':
            with self.f:
                writer = csv.writer(self.f)
                writer.writerows(xCsvClass.Datas)
                #xCsvClass.Datas.clear()
                DatasClear()
                #print(xCsvClass.Datas)
            # # self.fClose() # данные в csv файл пишутся в несколько проходов.
            # Поэтому файл закрывается ОДИН раз, а не после записи каждой строки

    # эти функции объявлены МЕТОДАМИ чтобы к ним можно было бы обращаться от имени объекта
    def printAll(self):
        i=0
        for data in xCsvClass.Datas:
            print(f'{i} --> {data}')
            i+=1

    def datasClear(self):
        xCsvClass.Datas.clear()

    def datasCopy(self, data):
        xCsvClass.Datas = data.copy()

    def valueToDatas(self, data):
        xCsvClass.Datas.append(data)

