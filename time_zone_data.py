import pandas as pd
dic
# Указываем путь к файлу Excel
excel_file = 'asddas.xlsx'

# Чтение данных из Excel-файла в DataFrame
df = pd.read_excel(excel_file)
first_column = df.iloc[:, 0]
# Выводим первые несколько строк DataFrame для проверки
print(first_column.head())
first_column_dict = first_column.to_dict()

for i in first_column_dict.items():
    print(i[1])