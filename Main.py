#Автор: Ушаков Илья Владимирович

#Программа позволяет выбрать рандомное блюдо из текстовых файлов
#В зависимости от категории либо из всех сразу
import random


#Функция для чтения файла и записи результата в массив
def readfile(filepath):
    array = []
    file = open(filepath, 'r', encoding='utf-8')
    for line in file:
        array.append(file.read().split('\n'))
    file.close()
    return array


#В скобочках стоят имена текстовых файлов, которые должны лежать в папке с файлом main.py
bake = readfile('Выпечка.txt')
potato = readfile('Картофель.txt')
porridge = readfile('Каши.txt')
pasta = readfile('Макароны.txt')
salad = readfile('Салаты.txt')
soup = readfile('Супы.txt')

#Засовывает все блюда из массивов в 1 общий
all= []
all.extend(bake)
all.extend(potato)
all.extend(porridge)
all.extend(pasta)
all.extend(salad)
all.extend(soup)

#"Интерфейс"
print('Выберите вариант...')
print('1 - Супы')
print('2 - Каши')
print('3 - Блюда из картофеля')
print('4 - Макароны')
print('5 - Салаты')
print('6 - Выпечка')
print('7 - Все')
print('Остальное - Выход')

#Ввод варианта для программы
option = input()


#Функция получения рандомного элемента массива
def randish(array):
    return array[random.randint(0, len(array) - 1)]


#"Эмуляция" switch-case с помощью словаря, аналога Map в java
value = {
    '1': randish(soup),
    '2': randish(porridge),
    '3': randish(potato),
    '4': randish(pasta),
    '5': randish(salad),
    '6': randish(bake),
    '7': randish(randish(all))
}
#Проверяет подходит ли ключ нашему вводу, если нет то тут по дефолту выходим
if option in value:
    print(value[option])
else:
    exit(0)