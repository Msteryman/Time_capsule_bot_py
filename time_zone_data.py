import pandas as pd

# Указываем путь к файлу Excel
excel_file = 'asddas.xlsx'

# Чтение данных из Excel-файла в DataFrame
df = pd.read_excel(excel_file)
first_column = df.iloc[:, 2]
# Выводим первые несколько строк DataFrame для проверки

first_column_dict = first_column.to_dict()
dict_1 = []
for i in first_column_dict.items():
    dict_1.append(i[1].replace('\xa0',''))

dict_2 = []
df = pd.read_excel(excel_file)
first_column = df.iloc[:, 0]
first_column_dict = first_column.to_dict()

for j,i in enumerate(first_column_dict.items()):
    i = list(i)
    if  type(i[1]) == float:
        i[1] = "null"
        dict_2.append(i[1])
    else:
        dict_2.append(i[1].replace('\xa0',''))
        


dict_final = dict(zip(dict_1,dict_2))
print(dict_final)
