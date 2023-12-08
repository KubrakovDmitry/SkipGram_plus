import xlsxwriter
from Word import Word

def outputExcel(dict, name):
    # Workbook () принимает один необязательный аргумент
    # это имя файла, которое мы хотим создать.

    workbook = xlsxwriter.Workbook('new' + name + '.xlsx') 

    
    # Затем объект книги используется для добавления нового
    # рабочий лист с помощью метода add_worksheet ().

    worksheet = workbook.add_worksheet() 

    
    # Создать новый объект Format для форматирования ячеек
    # в листах с использованием метода add_format ().

    
    # здесь мы создаем объект жирным шрифтом.

    bold = workbook.add_format({'bold': 1}) 

    
    # создать список данных.

    headings = ['слова', 'window = 2', 'window = 6']

    word = []
    value2 = []
    value6 = []

    for item in dict:
        word.append(item.word)
        value2.append(item.difvalue)
        value6.append(item.value)

    worksheet.write_row('A1', headings, bold) 

    
    # Написать столбец данных, начиная с
    # 'A2', 'B2', 'C2' соответственно.

    worksheet.write_column('A2', word) 

    worksheet.write_column('B2', value2) 

    worksheet.write_column('C2', value6) 

    
    # создание линейного графика

    chart1 = workbook.add_chart({'type': 'line'}) 

    # добавление серии 1

    chart1.add_series({ 

    'name':       ['Sheet1', 0, 1], 

    'categories': ['Sheet1', 1, 0, 20, 0], 

    'values':     ['Sheet1', 1, 1, 20, 1], 

    }) 

    # добавление серии 2

    chart1.add_series({ 

    'name':       ['Sheet1', 0, 2], 

    'categories': ['Sheet1', 1, 0, 20, 0], 

    'values':     ['Sheet1', 1, 2, 20, 2], 

    })

    # задание загаловка 

    chart1.set_title ({'name': name})

    # Добавить метку оси X

    chart1.set_x_axis({'name': 'Слова'}) 

    # Добавить метку оси Y

    chart1.set_y_axis({'name': 'Косинуская мера'}) 
    
    # Установить стиль диаграммы Excel.

    chart1.set_style(11) 

    
    # добавить таблицу к рабочему листу с учетом
    # значения смещения в верхнем левом углу
    # график привязан к ячейке D2.

    worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10}) 

    
    # Наконец, закройте файл Excel
    # с помощью метода close ().
    workbook.close()