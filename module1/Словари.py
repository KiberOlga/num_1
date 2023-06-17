"""english_dict = {
    "яблоко": "apple",
    "банан": "banana",
    "бамбук": "bamboo",
    "помело": "pomelo",
}
world = input("Введите слово на русском - ").lower()
if world in english_dict:
    print(world, "на английском будет ", english_dict[world])
else:
    print("Такого слова нет")"""


"""films_dict = {
    "Последний богатырь": "Виктор Хориняк",
    "Брат 2": "Сергей Бодров",
    "Форсаж": "Вин Дизель",
    "Жмурки": "Дмитрий Дюжев",
}
favourite_actor = input("Какой ваш любимый актёр? ")
film = input("Какой фильм вы хотите посмотреть? ")
actor = films_dict.get(film)
if actor ==favourite_actor:
    print("Этот фильм вам нужно посмотреть ")
else:
    print("Не то, что вам нужно ")"""

"""films_dict = {
    "Последний богатырь": "Виктор Хориняк",
    "Брат 2": "Сергей Бодров",
    "Форсаж": "Вин Дизель",
    "Жмурки": "Дмитрий Дюжев",
}
favourite_actor = input("Какой ваш любимый актёр? ")
film = input("Какой фильм вы хотите посмотреть? ")


if film in films_dict:
    actor = films_dict.get(film)
    if actor == favourite_actor:
        print("Этот фильм вам нужно посмотреть ")
    else:
        print("Не то, что вам нужно ")
else:
    print("Такого фильма у нас нет")"""


"""questions = [{
    "question": "Кто главный герой в аниме Джо Джо?",
    "answer": ["Джорно Джованна", "Джоске Хигашиката", "Джозеф Джоста", "Все три правильные варианты ответа", "Нет правильного"]
    "right_answer": 5
},
{
    "question": "Почему небо голубое?",
    "answer": ["Потому что гладиолус", "Длина волны синего света более короткая", "Маги наколдовали", "Все три правильные варианты ответа", "Нет правильного"]
    "right_answer": 2
},
{
    "question": "Кто придумал Python?",
    "answer": ["Марк Цукерберг", "Гвидо ван Россум", "Павел Дуров"]
    "right_answer": 2
},
{
    "question": "Кто такие фиксики?",
    "answer": ["Большой-большой секрет", "Дети помогатора", "Лунтик"]
    "right_answer": 1
},
{
    "question": "Что такое тикрейт?",
    "answer": ["Скорость получения и отправки пакетных данных", "Что-то в кс", "Бомба"]
    "right_answer": 1
},
    "Кто главный в аниме Джо Джо?", "Почему небо голубое?", "Кто придумал Python?", "Кто такие фиксики?", "Что такое тикрейт?"]
for question in questions:
    print(question.get("question"))
    answer_number = 0
    for answer in question["answer"]:
        answer_number += 1
        print(answer_number, ".", answer)
    user_answer = int(input("Ваш ответ: "))
    if user_answer == question.get("righ_answer"):
        print("Верно")
    else:
        print("Не верно")
    print("-" * 30)"""


"""questions = [{
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
    print("Ты проиграл!")"""


"""violator_songs = {
    "World in My Eyes": 4.86,
    "Sweetest Perfection": 4.43,
    "Personal Jesus": 4.56,
    "Halo": 4.9,
    "Waiting for the Night": 6.07,
    "Enjoy the Silence": 4.20,
    "Policy of Truth": 4.76,
    "Blue Dress": 4.29,
    "Clean": 5.83
}
amount = 0
a = int(input("Сколько песен выбрать? "))
for i in range(a):
    name = input("Название "+str(i+1)+" песни: ")
    duration = violator_songs[name]
    amount = amount + duration
print("Общее время звучания песен:",amount," минут")"""


"""goods = {
    "Лампа":'12345',
    "Стол":'23456',
    "Диван":'34567',
    "Стул":'45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for i in goods:
    s = 0
    for j in store[goods[i]]:
        s += j["quantity"] * j["price"]
    print(i,"-", j["quantity"], "штук", s)"""


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name, code in goods.items():
    thing_all_quantity = 0
    thing_all_cost = 0
    for product in store[code]:
        thing_quantity = product['quantity']
        thing_cost = product['price']
        thing_all_cost += thing_quantity * thing_cost
        thing_all_quantity += thing_quantity
    print('{0} - {1} шт, стоимость {2} рублей'.format(name, thing_all_quantity, thing_all_cost))
