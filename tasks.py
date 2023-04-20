"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""


'''Задание на закрепление знаний по модулю json. Есть файл orders в формате 
JSON с информацией о заказах. Написать скрипт, автоматизирующий его 
заполнение данными. Для этого: Создать функцию write_order_to_json(), 
в которую передается 5 параметров — товар (item), количество (quantity), 
цена (price), покупатель (buyer), дата (date). Функция должна 
предусматривать запись данных в виде словаря в файл orders.json. При записи 
данных указать величину отступа в 4 пробельных символа; Проверить работу 
программы через вызов функции write_order_to_json() с передачей в нее 
значений каждого параметра. """

3 tasl

Задание на закрепление знаний по модулю yaml. Написать скрипт, 
автоматизирующий сохранение данных в файле YAML-формата. Для этого: 
Подготовить данные для записи в виде словаря, в котором первому ключу 
соответствует список, второму — целое число, третьему — вложенный словарь, 
где значение каждого ключа — это целое число с юникод-символом, 
отсутствующим в кодировке ASCII (например, €); Реализовать сохранение данных 
в файл формата YAML — например, в файл file.yaml. При этом обеспечить 
стилизацию файла с помощью параметра default_flow_style, а также установить 
возможность работы с юникодом: allow_unicode = True; Реализовать считывание 
данных из созданного файла и проверить, совпадают ли они с исходными. 
'''

hm



import csv
import os
import re
def get_data():
    os_product_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = [
        ['Изготоитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file_name in ['info_1.txt', 'info_2.txt', 'info_3.txt']:
        with open(file_name, encoding='1251') as f:
            file_data = f.read()

        os_prod = re.search(r'Изготовиель системы:\s*(.*)', file_data)
        os_name = re.search(r'Название ОС:\s*(.*)', file_data)
        os_code = re.search(r'Код продукта:\s*(.*)', file_data)
        os_type = re.search(r'Тип системы:\s*(.*)', file_data)

        if os_product:
            os_prod_list.append(os_prod.group(1))
        if os_name:
            os_name_list.append(os_name.group(1))
        if os_code:
            os_code_list.append(os_code.group(1))
        if os_type:
            os_type_list.append(os_type.group(1))

        main_data.append([os_prod.group(1), os_name.group(1), os_code.group(1),
                          os_type.group(1)])

    return main_data
def write_to_csv(csv_file):
    main_data = get_data()

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(main_data)

csv_file = 'report.csv'
write_to_csv(csv_file)



import json
import chardet
def write_order_to_json(item, quantity, price, buyer, date):
    order = {"item": item, "quantity": quantity, "price": price,
             "buyer": buyer, "date": date}
    with open('orders.json', 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)['encoding']
    orders = json.loads(data.decode(encoding))
    orders['orders'].append(order)
    with open('orders.json', 'w', encoding=encoding) as f:
        f.write(json.dumps(orders, ensure_ascii=False, indent=4))
orders = [("Монитор", 2, 15000, "Сидоров С.С.", "2023-04-02"),
    ("Принтер", 1, 8000, "Иванов И.И.", "2023-04-04"),
    ("Сканер", 3, 10000, "Петров П.П.", "2023-04-01"),
    ("Ноутбук", 1, 50000, "Смирнов А.А.", "2023-04-03"),
    ("Клавиатура", 4, 2000, "Федоров Ф.Ф.", "2023-04-02"),
    ("Мышь", 5, 1000, "Григорьев Г.Г.", "2023-04-08"),
    ("Флешка", 10, 500, "Васильев В.В.", "2023-04-09"),
    ("Кресло", 2, 10000, "Дмитриев Д.Д.", "2023-04-05"),
    ("Стол", 1, 15000, "Кузнецов К.К.", "2023-04-07"),
    ("Коврик для мыши", 3, 500, "Макаров М.М.", "2023-04-01"),
    ("Блок питания", 1, 4000, "Романов Р.Р.", "2023-04-02"),
    ("Корпус", 1, 7000, "Лебедев Л.Л.", "2023-04-03"),
    ("Кулер для процессора", 2, 2500, "Белов Б.Б.", "2023-04-04"),
    ("Жесткий диск", 1, 10000, "Никитин Н.Н.", "2023-04-05"),
    ("Оперативная память", 2, 5000, "Орлов О.О.", "2023-04-08")]
for order in orders:
    write_order_to_json(*order)



import yaml
# Подготовка для записи в YAML
data = {
    "list": ["item1", "item2", "item3"],
    "integer": 1845,
    "dict": {
        "key1": 158,
        "key2": 200,
        "key3": ord("€")  # Юникод-символ €
}}
with open("file.yaml", "w", encoding="utf-8") as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

with open("file.yaml", "r", encoding="utf-8") as file:
    loaded_data = yaml.load(file, Loader=yaml.FullLoader)

if data == loaded_data:
    print("Данные совпадают")
else:
    print("Данные не совпадают")