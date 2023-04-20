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