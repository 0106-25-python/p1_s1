#ШАГ 1

file_object = open("db.txt", "r", encoding="utf8") #открываем файл на чтение
file_content = file_object.read() #читаем всё содержимое файла
file_object.close() #закрываем файл

db_lines = file_content.splitlines() #разбиваем всё содержимое по строками; возвращает список

counter = 1
for line in db_lines: #запускаем цикл по списку; перебираем строки
	final_output = "Задача " + str(counter) + ": " + line
	print(final_output)
	counter += 1