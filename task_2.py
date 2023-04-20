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