#ШАГ 3

def read_from_db():
	file_object = open("db.txt", "r", encoding="utf8")
	file_content = file_object.read()
	file_object.close()
	return file_content

def parse_tasks(raw_content):
	raw_tasks = raw_content.splitlines()
	#raw_tasks = raw_content.split("\n")
	tasks = [] #создаём пустой список

	for task_info in raw_tasks:
		splitted_task = task_info.split("<>") #разбиваем строку по сепаратору
		raw_status = splitted_task[4]
		if raw_status == "active": #проверяем статус
			status = "✓"
		else:
			status = "✕"
		task = status + " " + splitted_task[1] + " " + splitted_task[2] + " " + splitted_task[3] #формируем итоговую строку для вывода в консоль
		tasks.append(task) #добавляем элемент в список

	return tasks

def print_all_tasks(tasks):
	counter = 1
	print("Актуальные задачи:")
	for task_info in tasks:
		print(str(counter) + ": " + task_info)
		counter += 1

all_tasks = read_from_db()
tasks_list = parse_tasks(all_tasks)
print_all_tasks(tasks_list)