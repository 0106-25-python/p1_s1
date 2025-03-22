## Итоговый результат работы программы
- Чтение информации из файла с определённой структурой
- Переработка и вывод на экран информации в следующем виде\
![Итоговый вывод](p1_s1_final.png)

статус задачи выводим в виде символа:
- active - ✓
- done - ✕

Шаг 1
Чтение информации из файла и вывод в консоль в формате
(скриншот вывода)

Что нам пригодится из возможностей Python
1) Функция [open()](https://www.w3schools.com/python/python_file_open.asp)

```python
file_object = open("db.txt", "r") #открываем файл на чтение; инициализируем переменную, которая содержит объект файл
file_content = file_object.read() #инициализируем переменную, которой присваивается весь контент файла
file_object.close() #всегда хорошая практика закрывать файл после действий с его контентом, если не планируете больше что-то с ним делать
```

2) Функция [splitlines()](https://www.w3schools.com/python/ref_string_splitlines.asp)

```python
string_to_list = """Это первая строка.
Это вторая строка."""
splitted_string = string_to_list.splitlines() #вызов функции возвращает список, состоящий из 2-х строк
```

3) Использование циклов с помощью конструкции [for](https://www.w3schools.com/python/python_for_loops.asp)
```python
string_to_list = """Это первая строка.
Это вторая строка."""
splitted_string = string_to_list.splitlines()
for specific_line in splitted_string: #запускаем цикл с перебором списка
  print(specific_line) #выводим конкретный элемент из списка
```

4) Вывод информации в консоль с помощью функции [print()](https://www.w3schools.com/python/ref_func_print.asp)
```python
print("Простой вывод строки")
```
