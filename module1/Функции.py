"""file = open("file.txt", "w")
file.write("Тестирование по фильмам")
file.close()
name = input()
questions = [{
    'question': 'Кто главный герой в аниме "Джо Джо"?',
    'answer': ['Джорно Джованна', 'Джоске Хигашиката', 'Джозеф джоста',
               'Нет правильного варианта ответа', 'Все из перечисленных'],
    'right_answer': 5
    },
    {
        'question': 'Формула дискриминанта',
        'answer': ['b^2-4ac', 'b-4ac', 'b^2-2ac'],
        'right_answer': 1
    },
    {
        'question': 'Почему небо голубое?',
        'answer': ['Потому что гладиолус', 'длина волны синего цвета более короткая',
                   'Маги наколдовали'],
        'right_answer': 2
    }, {
        'question': 'Кто придумал питон?',
        'answer': ['Марк Цукерберг', 'Гвидо ван Россум', 'Павел Дуров', 'Питон'],
        'right_answer': 2
    }, {
        'question': 'Кто такие фиксики?',
        'answer': ['Большой-большой секрет', 'Дети помогатора', 'Лунтик', 'Баба Капа'],
        'right_answer': 1
    }, {
        'question': 'Что такое тикрейт?',
        'answer': ['что то в кс', 'Бомба', 'синоним слова арбуз',
                     'Cкорость получения и отправки пакетных данных'],
        'right_answer': 4
    }, {
        'question': 'Кто создал Google?',
        'answer': ['Ларри Пейдж', 'Сергей Брин', 'Все из перечисленных'],
        'right_answer': 3
    }, {
        'question': 'Что такое ПК?',
        'answer': ['Персональный компьютер', 'Мышь', 'Аттракцион'],
        'right_answer': 1
    }
]
mates = 0
for question in questions:
    print(question.get('question'))
    answer_number = 0
    for answer in question['answer']:
        answer_number += 1
        print(answer_number, '.', answer)
    user_answer = int(input('Ваш ответ: '))
    if user_answer == question.get('right_answer'):
        print('Верно')
        mates += 1
    else:
        print('Не верно')
    print('-' * 30)
print('Верных ответов: ', mates)
if mates >= 3:
    print("Ты победил!")
else:
    print("Ты проиграл!")
file = open("file.txt","a")
file.write("Игрок" + name + "набрал" + str(mates) + "очков./n")
file.close()
information = file.read()
print(information)"""


"""with open("file.txt") as f:
    for line in f.readlines():
        print(line)

file = open("file.txt")
massive = [int(i) for i in file]
print(massive)"""


"""with open("file.txt") as f:
    for line in f.readlines():
        print(line)

file = open("file.txt")
massive = [int(i) for i in file]
print(massive)"""


"""import math
file = open("numbers.txt", "w")
numbers = [int(input()) for i in range(7)]
result = 0
for number in numbers:
    result += math.factorial(number) - math.sqrt(number)
    file.write(str(number))
file.close()"""


"""def Calculate(x, y):
    sign = input("Введите арифметический знак ")
    if sign == "+":
        return x + y
    return x - y
print(Calculate(19, 7))
def Calculate2(x, y):
    return x + y, x - y
print(Calculate(30, 17))"""


"""def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return year // 10
    else:
        return year // 10
for year in range(1800, 2023):
    if leap_year(year) >= 195:
    print(year, leap_year(year))"""


"""N = int(input('Введите число: '))
def summa_n(N):
    if N == 0:
        return N
    else:
        return(N + summa_n(N-1))
print(f"Сумма чисел от 1 до {N} равна {summa_n(N)}")"""


"""def calculate(x,y,a):
    if a == '+':
        return x + y
    elif a == '-':
        return x - y
    elif a == '*':
        return x * y
    elif a == '/':
        return x / y
a = input("Введите арифметический знак ")
x = int(input("Введите первое число "))
y = int(input("Введите второе число "))
e = calculate(x, y, a)
print(e)
file = open('calculations.txt', 'a')
file.write(f'{e}' + '\n')"""


def greeting(a):
    if a == 'Да':
        print('Привет!')
        print('Добро пожаловать!')
for i in range(5):
    a = input('Зайдёте? Да/Нет: ')
    greeting(a)
    print('Следующий.\n')







