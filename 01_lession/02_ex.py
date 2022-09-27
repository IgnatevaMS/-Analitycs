# Написать функцию для нахождения одинаковых элементов в двух списках
list1 = ['мама', 'мыла', 'раму']
list2 = ['мама','не домыла']

for i in list1:
    for j in list2:
        if i.startswith(j):
            print(i)
            break