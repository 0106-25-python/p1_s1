#ШАГ 2

def read_from_db(): #функция для чтения контента из БД
	file_object = open("db.txt", "r", encoding="utf8")
	file_content = file_object.read()
	file_object.close()
	return file_content #возвращаем содержимое файла

def parse_tasks(raw_content): #функция для преобразования контента в список информации о задачах
	tasks = raw_content.splitlines()
	return tasks #возвращаем список

def print_all_tasks(tasks): #функция для вывода на экран 
	counter = 1
	for task_info in tasks:
		print("Задача " + str(counter) + ": " + task_info)
		counter += 1

#запускаем последовательность вызовов функций
all_tasks = read_from_db() #вызываем первую функцию
tasks_list = parse_tasks(all_tasks) #вызываем вторую функцию
print_all_tasks(tasks_list) #вызываем третью функцию