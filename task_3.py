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