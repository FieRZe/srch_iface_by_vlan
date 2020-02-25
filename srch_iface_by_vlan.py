# -*- coding: utf-8 -*-

import re
from datetime import datetime

start = datetime.now()

##################################
# Открываем файл, создаем list

cfg = "cisco-local.conf"

mylines = []

with open(cfg) as o_cfg:

	for line in o_cfg:
		mylines.append(line.rstrip('\n')) ### каждую линию добавляем в конец листа 

##############################
# Все что нам надо было мы взяли из файла, сохнарили в list mylines
# Но по логике у нас весь текстовый документ сейчас в виде листа в переменной mylines.
# Т.е. все еще не есть good можно ли хранить меньше объем данных?



while True: 	# Запускаем цикл с возможностью ввода множества vlan-ов, по очереди
	
	user_input = input("Введите VLAN id: ")
	
	if user_input == "q" or user_input == "й": # для выхода нажми q или й
		break

	elif user_input == "":
		continue 	### для любителей потыкать Enter перед вводом чего-либо

	###### Проверяем не ввел ли пользователь какую-то хрень	
	else: 
		try:
			user_input == int(user_input) 
		except (ValueError): ## если не integer будет ошибка ValueError, меняем ее на инструкцию
			print ("\nНедопустимые символы!\nДопускаются только целые числа")
			print ("Для выхода из программы введите 'q' + Enter\n")		
		else: 
			##### Если введенный номер VLAN не существует в list будет другая ошибка ValueError
			##### заменяем ошибку на удобную инструкцию:
			try:
				###### Одновременно с проверкой задаем новую переменную index
				###### index = номер элемента под которым находится этот элемент в листе mylines[x]. 
				###### Должно совпадать символ в символ иначе - ошибка
				index = mylines.index("interface GigabitEthernet0/0." + user_input)
			except (ValueError):
				print ("\nТакого VLAN нет в базе.")
				print ("Проверьте правильно ли введен VLAN id\n")		
			
			##### Если VLAN есть в базе: найти строку, и начать выводить list пока не упремся в "!"
			else:
				print("")
				while True:
					#### индекс мы задали выше
					#### теперь мы выводим все последующие строки = строка + 1
					#### пока index не будет равен элементу "!"
					if mylines[index] == "!": 
						break
					print(mylines[index])
					index += 1
				print("")

end = datetime.now() - start
print(end)
