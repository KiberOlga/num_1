# -*- coding: cp1251 -*-
from datetime import datetime
import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, меня зовут Квант, я твой голосовой ассистент.')
print('Привет, меня зовут Квант, я твой голосовой ассистент.')
voice.runAndWait()

while True:
    with sr.Microphone() as source:
        print('Слушаю...')
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language='ru_RU').lower()
        print('Вы сказали -  ', speech)

    except:
        voice.say('ничего не слышу')
        voice.runAndWait()
        break

    if speech.find('привет') >= 0 or speech.find('добрый день') >= 0:
        greeting = ["Привет!", "Добрый день!", "Hello!", "Hi!", "Good afternoon!"]
        gr = random.choice(greeting)
        voice.say(gr + "рад тебя слышать")
        voice.runAndWait()

    elif speech.find('что ты умеешь') >= 0 or speech.find('чем можешь помочь') >= 0 or speech.find('что ты можешь') >= 0:
        voice.say("Я могу помочь подготовиться к сдаче ОГЭ по физике")
        voice.runAndWait()

    elif speech.find('youtube') >= 0 or speech.find('ютуб') >= 0:
        webbrowser.open_new('https://www.youtube.com/')
        voice.say('Я открыл ютуб')
        voice.runAndWait()

    elif speech.find('фильм') >= 0:
        films = ["Титаник", "Последний богатырь", "Чебурашка", "Непослушник", "Конёк - горбунок"]
        gr = random.choice(films)
        voice.say("Я тебе советую посмотреть фильм " + gr + ". Он очень интересный и позновательный.")
        voice.runAndWait()

    elif speech.find('учи ру') >= 0:
        webbrowser.open_new('https://uchi.ru/')
        voice.say('Я открыл учи ру')
        voice.runAndWait()

    elif speech.find('маил') >= 0 or speech.find('почта') >= 0 or speech.find('почту') >= 0:
        webbrowser.open_new('https://mail.ru/')
        voice.say('Я открыл почту mail')
        voice.runAndWait()

    elif speech.find('решу ОГЭ') >= 0 or speech.find('решу огэ') >= 0:
        webbrowser.open_new('https://phys-oge.sdamgia.ru/')
        voice.say('Я открыл сайт решу ОГЭ')
        voice.runAndWait()

    elif speech.find('фипи') >= 0 or speech.find('fipi') >= 0:
        webbrowser.open_new('https://fipi.ru/oge/otkrytyy-bank-zadaniy-oge#!/tab/173942232-3')
        voice.say('Я открыл сайт фипи')
        voice.runAndWait()

    elif speech.find('молодец') >= 0 or speech.find('умница') >= 0 or speech.find('спасибо') >= 0:
        compliment = ["И вам спасибо, обращайтесь", "Обращайтесь, буду рад помочь", "Приятно иметь дело с вежливым человеком", "Спасибо за доверие, обращайтесь"]
        c = random.choice(compliment)
        voice.say(c)
        voice.runAndWait()

    elif speech.find('алиса') >= 0 or speech.find('окей гугл') >= 0 or speech.find('ok google') >= 0:
        voice.say("Очень смешно, обхохочешься")
        voice.runAndWait()

    elif speech.find('сколько тебе лет') >= 0 or speech.find('возраст') >= 0:
        voice.say("у меня сегодня день рождение, мне исполняется 7 лет, так что с вас подарок")
        voice.runAndWait()

    elif speech.find('как тебя зовут') >= 0 or speech.find('как твоё имя') >= 0:
        voice.say("хоть мы уже познакомились, я напомню своё имя, меня зовут Квант")
        voice.runAndWait()

    elif speech.find('время') >= 0 or speech.find("какой сейчас час") >= 0 or speech.find("времени") >= 0:
        today = datetime.now()
        today = today.strftime("%H:%M:%S")
        voice.say(f"На данный момент {today}")
        voice.runAndWait()

    elif speech.find('видео') >= 0:
        speech = speech.replace("видео", "")
        url = "https://www.youtube.com/results?search_query=" + speech
        webbrowser.get().open(url)
        voice.say("Я открыл " + speech + "на youtube")
        voice.runAndWait()

    elif speech.find('google') >= 0 or speech.find('гугл') >= 0:
        speech = speech.replace("google", "")
        url = "https://www.google.com/search?q=" + speech
        webbrowser.get().open(url)
        voice.say("Я открыл " + speech + "в Google")
        voice.runAndWait()



    elif speech.find('молекула') >= 0:
        voice.say("Молекула - это мельчайшая частица данного вещества")
        voice.runAndWait()

    elif speech.find('скорость') >= 0:
        voice.say("Скорость (?) — физическая величина, численно равна пути (S), пройденного телом за единицу времени (t). v = S делёное на t")
        voice.runAndWait()

    elif speech.find('сила тяжести') >= 0:
        voice.say("Сила тяжести — сила (FТ), с которой Земля притягивает к себе тело, равная произведению массы (т) тела на коэффициент пропорциональности (g) — постоянную величину для Земли. (g = 9,8 H/кг)FТ = m*g")
        voice.runAndWait()

    elif speech.find('вес') >= 0:
        voice.say("Вес (Р) — сила, с которой тело действует на горизонтальную опору или вертикальный подвес, равная произведению массы (т) тела на коэффициент (g).Р = m*g")
        voice.runAndWait()

    elif speech.find('масса') >= 0:
        voice.say("Масса (т) — мера инертности тела, определяемая при его взвешивании как отношение силы тяжести (Р) к коэффициенту (g).т = Р / g")
        voice.runAndWait()

    elif speech.find('плотность') >= 0:
        voice.say("Плотность (r) — масса единицы объёма вещества, численно равная отношению массы (т) вещества к его объёму (V).r = m / V")
        voice.runAndWait()

    elif speech.find('давление') >= 0:
        voice.say("Давление (р) — величина, численно равная отношению силы (F), действующей перпендикулярно поверхности, к площади (S) этой поверхностиp = F / S")
        voice.runAndWait()

    elif speech.find('закон Архимеда') >= 0:
        voice.say("На тело, погруженное в жидкость (или газ), действует выталкивающая сила — архимедова сила (FВ). равная весу жидкости (или газа), в объёме (VТ) этого тела.FВ = r*g*Vт")
        voice.runAndWait()

    elif speech.find('механическая работа') >= 0:
        voice.say("Работа (A) — величина, равная произведению перемещения тела (S) на силу (F), под действием которой это перемещение произошло.")
        voice.runAndWait()

    elif speech.find('потенциальная энергия') >= 0:
        voice.say("Потенциальная энергия (ЕП) тела, поднятого над Землей, пропорциональна его массе (т) и высоте (h) над Землей.ЕП = m*g*h")
        voice.runAndWait()

    elif speech.find('кинетическая энергия') >= 0:
        voice.say("Кинетическая энергия (ЕК) движущегося тела пропорциональна его массе (m) и квадрату скорости (v2) ЕК = m*v2 / 2")
        voice.runAndWait()

    elif speech.find('мощность') >= 0:
        voice.say("Мощность (N) — величина, показывающая скорость выполнения работы и равная а) отношению работы (А) ко времени (t), за которое она выполнена;б) произведению силы (F), под действием которой перемещается тело, на среднюю скорость (?) его перемещения.")
        voice.runAndWait()

    elif speech.find('диффузия') >= 0:
        voice.say("Диффузия – это взаимное проникновение одного вещества между молекулами другого.")
        voice.runAndWait()

    elif speech.find('тепловые явления') >= 0:
        voice.say("Явления, связанные с нагреванием или охлаждением тел, с изменением температуры.")
        voice.runAndWait()

    elif speech.find('тепловое движение') >= 0:
        voice.say("Процесс беспорядочного движения частиц, образующих вещество. Чем выше температура, тем больше скорость движения частиц.")
        voice.runAndWait()

    elif speech.find('закон сохранения энергии') >= 0:
        voice.say("Во всех явлениях, происходящих в природе, энергия не возникает из ниоткуда и не исчезает в никуда. Она может только превращаться из одного вида в другой, при этом её значение сохраняется.")
        voice.runAndWait()

    elif speech.find('внутренняя энергия') >= 0:
        voice.say("Сумма кинетических энергий всех молекул, из которых состоит тела, и потенциальных энергий их взаимодействий.")
        voice.runAndWait()

    elif speech.find('теплопередача') >= 0:
        voice.say("Процесс изменения внутренней энергии без совершения работы на телом или самим телом.")
        voice.runAndWait()

    elif speech.find('теплопроводность') >= 0:
        voice.say("Явление передачи внутренней энергии от одной части тела к другой или от одного тела к другому при их непосредственном контакте.")
        voice.runAndWait()

    elif speech.find('конвекция') >= 0:
        voice.say("Вид теплопередачи, при которых энергия переносится струями газа или жидкости.")
        voice.runAndWait()

    elif speech.find('плавление') >= 0:
        voice.say("Переход из твёрдого состояния в жидкое.")
        voice.runAndWait()

    elif speech.find('парообразование') >= 0:
        voice.say("Переход из жидкого состояния в газообразное (из жидкости в пар).")
        voice.runAndWait()

    elif speech.find('испарение') >= 0:
        voice.say("Парообразование, происходящие с поверхности жидкости.")
        voice.runAndWait()

    elif speech.find('насыщенный пар') >= 0:
        voice.say("Пар, находящийся в динамическом равновесии со своей жидкостью.")
        voice.runAndWait()

    elif speech.find('конденсация') >= 0:
        voice.say("Переход из газообразного состояния в жидкое (из пара в жидкость).")
        voice.runAndWait()

    elif speech.find('кипение') >= 0:
        voice.say("Интенсивный переход жидкости в пар, происходящий с образованием пузырьков пара по всему объёму жидкости при определённой температуре.")
        voice.runAndWait()

    elif speech.find('точка росы') >= 0:
        voice.say("Температура, при которой пар, находящийся в воздухе, становится насыщенным.")
        voice.runAndWait()

    elif speech.find('электрическое поле') >= 0:
        voice.say("Особый вид материи, отличающийся от вещества.")
        voice.runAndWait()

    elif speech.find('электрическая сила') >= 0:
        voice.say("Сила, с которой электрическое поле действует на внесённый в него электрический заряд.")
        voice.runAndWait()

    elif speech.find('электрон') >= 0:
        voice.say("Частица, имеющая самый маленький заряд. Заряд электрона отрицательный, ?1.6·10?19 Кл.")
        voice.runAndWait()

    elif speech.find('закон сохранения заряда') >= 0:
        voice.say("Алгебраическая сумма электрических зарядов остаётся постоянной при любых взаимодействиях в замкнутой системе.")
        voice.runAndWait()

    elif speech.find('проводники') >= 0:
        voice.say("Тела, через которые электрические заряды могут переходить от заряженного тела к незаряженному. В проводниках есть свободные заряды.")
        voice.runAndWait()

    elif speech.find('непроводники') >= 0:
        voice.say("Тела, через которые электрические заряды не могут переходить от заряженного тела к незаряженному.")
        voice.runAndWait()

    elif speech.find('электрический ток') >= 0:
        voice.say("Упорядоченное направленное движение заряженных частиц.")
        voice.runAndWait()

    elif speech.find('сила тока') >= 0:
        voice.say("Отношение электрического заряда q, прошедшего через поперечное сечение проводника, ко времени его прохождения t.")
        voice.runAndWait()

    elif speech.find('напряжение') >= 0:
        voice.say("Показывает, какую работу совершает электрическое поле при перемещении единичного положительного заряда из одной точки в другую.")
        voice.runAndWait()

    elif speech.find('электрическое сопротивление') >= 0:
        voice.say("Физическая величина, характеризующая свойство проводника препятствовать прохождению электрического тока и равная отношению напряжения на концах проводника к силе тока, протекающего по нему.")
        voice.runAndWait()

    elif speech.find('закон Ома') >= 0 or speech.find('закон ома') >= 0:
        voice.say("Сила тока в участке цепи прямо пропорциональна напряжению на его концах и обратно пропорциональна его сопротивлению.")
        voice.runAndWait()

    elif speech.find('удельное сопротивление') >= 0:
        voice.say("Физическая величина, определяющая сопротивление проводника из данного вещества длиной 1 м и площадью поперечного сечения 1 м2.")
        voice.runAndWait()

    elif speech.find('короткое замыкание') >= 0:
        voice.say("Соединение концов участка цепи проводником, сопротивление которого очень мало по сравнению с сопротивлением участка цепи.")
        voice.runAndWait()



    elif speech.find('пока') >= 0 or speech.find('бай') >= 0:
        voice.say('Пока! До скорой встречи!')
        voice.runAndWait()
        break

    elif speech.find('') >= 0:
        speech = speech.replace("google", "")
        url = "https://www.google.com/search?q=" + speech
        webbrowser.get().open(url)
        voice.say("Такое я ещё пока не знаю, но поискал " + speech + "в Google")
        voice.runAndWait()
        break
