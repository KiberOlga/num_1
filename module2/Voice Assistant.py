# -*- coding: cp1251 -*-
"""import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import webbrowser

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("������! � ���� ���������!")
voice.runAndWait()


while True:
    with sr.Microphone() as sourse:
        print("����� ��������")
        audio = r.listen(sourse)
    try:
        speech = r.recognize_google(audio, language="ru_Ru").lower()
        print("�� ������� - ", speech)
    except:
        voice.say("������ �� �����")
        voice.runAndWait()
        break

    if speech.find("������") >= 0 or speech.find("������ ����") >= 0:
        voice.say("������")
        voice.runAndWait()

    elif speech.find("����") >= 0 or speech.find("youtube"):
        webbrowser.open_new("https://www.youtube.com/")
        voice.say("� ������� ����")
        voice.runAndWait()

    elif speech.find("����") >= 0:
        os.startfile("jetbrains://pycharm/navigate/reference?project=Tg_bot.py&path=module2/file.txt")
        voice.say("���� ������")
        voice.runAndWait()

    elif speech.find("����") >= 0 or speech.find("���"):
        voice.say("����")
        voice.runAndWait()
        break

#print(sr.Microphone.list_working_microphones())"""






"""import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import webbrowser

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('������, � ���� ���������')
voice.runAndWait()

while True:
    with sr.Microphone() as source:
        print('����� ��������')
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language='ru_RU').lower()
        print('�� ������� -  ', speech)

    except:
        voice.say('������ �� �����')
        voice.runAndWait()
        break

    if speech.find('������') >= 0 or speech.find('������ ����') >= 0:
        voice.say('������!')
        voice.runAndWait()

    elif speech.find('youtube') >= 0 or speech.find('����') >= 0:
        webbrowser.open_new('https://www.youtube.com/')
        voice.say('� ������� ����')
        voice.runAndWait()

    elif speech.find('����') >= 0:
        os.startfile("jetbrains://pycharm/navigate/reference?project=Tg_bot.py&path=module2/file.txt")
        voice.say('���� ������')
        voice.runAndWait()

    elif speech.find('����') >= 0 or speech.find('���'):
        voice.say('����!')
        voice.runAndWait()
        break"""




"""import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('������! ���� ����� �����. � ���� ���������.')
voice.runAndWait()

while True:
    with sr.Microphone() as source:
        print('����� ��������')
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language='ru_RU').lower()
        print('�� ������� -  ', speech)

    except:
        voice.say('������ �� �����')
        voice.runAndWait()
        break

    if speech.find('������') >= 0 or speech.find('������ ����') >= 0:
        greeting = ["������!", "������ ����!", "Hello!", "Hi!", "Good afternoon!"]
        gr = random.choice(greeting)
        voice.say(gr)
        voice.runAndWait()

    elif speech.find('youtube') >= 0 or speech.find('����') >= 0:
        webbrowser.open_new('https://www.youtube.com/')
        voice.say('� ������� ����')
        voice.runAndWait()

    elif speech.find('����') >= 0:
        os.startfile("jetbrains://pycharm/navigate/reference?project=Tg_bot.py&path=module2/file.txt")
        voice.say('���� ������')
        voice.runAndWait()

    elif speech.find('����') >= 0 or speech.find('���'):
        voice.say('����!')
        voice.runAndWait()
        break"""




"""import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('������! ���� ����� �����. � ���� ���������.')
voice.runAndWait()

while True:
    with sr.Microphone() as source:
        print('����� ��������')
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language='ru_RU').lower()
        print('�� ������� -  ', speech)

    except:
        voice.say('������ �� �����')
        voice.runAndWait()
        break

    if speech.find('������') >= 0 or speech.find('������ ����') >= 0:
        greeting = ["������!", "������ ����!", "Hello!", "Hi!", "Good afternoon!"]
        gr = random.choice(greeting)
        voice.say(gr)
        voice.runAndWait()

    elif speech.find('youtube') >= 0 or speech.find('����') >= 0:
        webbrowser.open_new('https://www.youtube.com/')
        voice.say('� ������� ����')
        voice.runAndWait()

    elif speech.find('����') >= 0:
        os.startfile("jetbrains://pycharm/navigate/reference?project=Tg_bot.py&path=module2/file.txt")
        voice.say('���� ������')
        voice.runAndWait()

    elif speech.find('�����') >= 0:
        films = ["�������", "��������� ��������", "���������", "�����������", "���� - ��������"]
        gr = random.choice(films)
        voice.say("� ���� ������� ���������� ����� " + gr + ". �� ����� ���������� � ��������������.")
        voice.runAndWait()

    elif speech.find('����') >= 0 or speech.find('���'):
        voice.say('����!')
        voice.runAndWait()
        break"""





import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('������, ���� ����� �����, � ���� ��������� ��������.')
voice.runAndWait()

while True:
    with sr.Microphone() as source:
        print('����� ��������')
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language='ru_RU').lower()
        print('�� ������� -  ', speech)

    except:
        voice.say('������ �� �����')
        voice.runAndWait()
        break

    if speech.find('������') >= 0 or speech.find('������ ����') >= 0:
        greeting = ["������!", "������ ����!", "Hello!", "Hi!", "Good afternoon!"]
        gr = random.choice(greeting)
        voice.say(gr + "� ��� ����� �������� ����� �����������")
        voice.runAndWait()

    elif speech.find('youtube') >= 0 or speech.find('����') >= 0:
        webbrowser.open_new('https://www.youtube.com/')
        voice.say('� ������� ����')
        voice.runAndWait()

    elif speech.find('����') >= 0:
        os.startfile("jetbrains://pycharm/navigate/reference?project=Tg_bot.py&path=module2/file.txt")
        voice.say('���� ������')
        voice.runAndWait()

    elif speech.find('�����') >= 0:
        films = ["�������", "��������� ��������", "���������", "�����������", "���� - ��������"]
        gr = random.choice(films)
        voice.say("� ���� ������� ���������� ����� " + gr + ". �� ����� ���������� � ��������������.")
        voice.runAndWait()

    elif speech.find('��� ��') >= 0:
        webbrowser.open_new('https://uchi.ru/')
        voice.say('� ������� ��� ��')
        voice.runAndWait()

    elif speech.find('����') >= 0 or speech.find('�����') >= 0 or speech.find('�����') >= 0:
        webbrowser.open_new('https://mail.ru/')
        voice.say('� ������� ����� mail')
        voice.runAndWait()

    elif speech.find('���� ���') >= 0:
        webbrowser.open_new('https://ege.sdamgia.ru/')
        voice.say('� ������� ���� ���� ���')
        voice.runAndWait()

    elif speech.find('�������') >= 0 or speech.find('������') >= 0 or speech.find('�������') >= 0:
        compliment = ["� ��� �������, �� ����� ������� �������", "������� ���� ������, ��� �������", "������� ����� ���� � �������� ���������", "������� �� �������, �����������"]
        c = random.choice(compliment)
        voice.say(c)
        voice.runAndWait()

    elif speech.find('�����') >= 0 or speech.find('���� ����') >= 0  or speech.find('ok google') >= 0:
        voice.say("����� ������, ������������")
        voice.runAndWait()

    elif speech.find('������� ���� ���') >= 0 or speech.find('�������') >= 0:
        voice.say("� ���� ������� ���� ��������, ��� ����������� 14 ���, ��� ��� � ��� �������")
        voice.runAndWait()

    elif speech.find('��� ���� �����') >= 0 or speech.find('��� ��� ���') >= 0:
        voice.say("��� ������� � ��� �������� � �������, �� ��� �������������")
        voice.runAndWait()






    elif speech.find('��������') >= 0:
        voice.say("�������� - ��� ���������� ������� ������� ��������")
        voice.runAndWait()

    elif speech.find('��������') >= 0:
        voice.say("�������� (?) � ���������� ��������, �������� ����� ���� (S), ����������� ����� �� ������� ������� (t). v = S ������ �� t")
        voice.runAndWait()

    elif speech.find('���� �������') >= 0:
        voice.say("���� ������� � ���� (F�), � ������� ����� ����������� � ���� ����, ������ ������������ ����� (�) ���� �� ����������� ������������������ (g) � ���������� �������� ��� �����. (g = 9,8 H/��)F� = m*g")
        voice.runAndWait()

    elif speech.find('���') >= 0:
        voice.say("��� (�) � ����, � ������� ���� ��������� �� �������������� ����� ��� ������������ ������, ������ ������������ ����� (�) ���� �� ����������� (g).� = m*g")
        voice.runAndWait()

    elif speech.find('�����') >= 0:
        voice.say("����� (�) � ���� ���������� ����, ������������ ��� ��� ����������� ��� ��������� ���� ������� (�) � ������������ (g).� = � / g")
        voice.runAndWait()

    elif speech.find('���������') >= 0:
        voice.say("��������� (r) � ����� ������� ������ ��������, �������� ������ ��������� ����� (�) �������� � ��� ������ (V).r = m / V")
        voice.runAndWait()

    elif speech.find('��������') >= 0:
        voice.say("�������� (�) � ��������, �������� ������ ��������� ���� (F), ����������� ��������������� �����������, � ������� (S) ���� �����������p = F / S")
        voice.runAndWait()

    elif speech.find('����� ��������') >= 0:
        voice.say("�� ����, ����������� � �������� (��� ���), ��������� ������������� ���� � ���������� ���� (F�). ������ ���� �������� (��� ����), � ������ (V�) ����� ����.F� = r*g*V�")
        voice.runAndWait()

    elif speech.find('������������ ������') >= 0:
        voice.say("������ (A) � ��������, ������ ������������ ����������� ���� (S) �� ���� (F), ��� ��������� ������� ��� ����������� ���������.")
        voice.runAndWait()

    elif speech.find('������������� �������') >= 0:
        voice.say("������������� ������� (��) ����, ��������� ��� ������, ��������������� ��� ����� (�) � ������ (h) ��� ������.�� = m*g*h")
        voice.runAndWait()

    elif speech.find('������������ �������') >= 0:
        voice.say("������������ ������� (��) ����������� ���� ��������������� ��� ����� (m) � �������� �������� (v2) �� = m*v2 / 2")
        voice.runAndWait()

    elif speech.find('��������') >= 0:
        voice.say("�������� (N) � ��������, ������������ �������� ���������� ������ � ������ �) ��������� ������ (�) �� ������� (t), �� ������� ��� ���������;�) ������������ ���� (F), ��� ��������� ������� ������������ ����, �� ������� �������� (?) ��� �����������.")
        voice.runAndWait()

    elif speech.find('��������') >= 0:
        voice.say("�������� � ��� �������� ������������� ������ �������� ����� ���������� �������.")
        voice.runAndWait()

    elif speech.find('�������� �������') >= 0:
        voice.say("�������, ��������� � ����������� ��� ����������� ���, � ���������� �����������.")
        voice.runAndWait()

    elif speech.find('�������� ��������') >= 0:
        voice.say("������� �������������� �������� ������, ���������� ��������. ��� ���� �����������, ��� ������ �������� �������� ������.")
        voice.runAndWait()

    elif speech.find('����� ���������� �������') >= 0:
        voice.say("�� ���� ��������, ������������ � �������, ������� �� ��������� �� �������� � �� �������� � ������. ��� ����� ������ ������������ �� ������ ���� � ������, ��� ���� � �������� �����������.")
        voice.runAndWait()

    elif speech.find('���������� �������') >= 0:
        voice.say("����� ������������ ������� ���� �������, �� ������� ������� ����, � ������������� ������� �� ��������������.")
        voice.runAndWait()

    elif speech.find('�������������') >= 0:
        voice.say("������� ��������� ���������� ������� ��� ���������� ������ �� ����� ��� ����� �����.")
        voice.runAndWait()

    elif speech.find('����������������') >= 0:
        voice.say("������� �������� ���������� ������� �� ����� ����� ���� � ������ ��� �� ������ ���� � ������� ��� �� ���������������� ��������.")
        voice.runAndWait()

    elif speech.find('���������') >= 0:
        voice.say("��� �������������, ��� ������� ������� ����������� ������� ���� ��� ��������.")
        voice.runAndWait()

    elif speech.find('���������') >= 0:
        voice.say("������� �� ������� ��������� � ������.")
        voice.runAndWait()

    elif speech.find('���������������') >= 0:
        voice.say("������� �� ������� ��������� � ������������ (�� �������� � ���).")
        voice.runAndWait()

    elif speech.find('���������') >= 0:
        voice.say("���������������, ������������ � ����������� ��������.")
        voice.runAndWait()

    elif speech.find('���������� ���') >= 0:
        voice.say("���, ����������� � ������������ ���������� �� ����� ���������.")
        voice.runAndWait()

    elif speech.find('�����������') >= 0:
        voice.say("������� �� ������������� ��������� � ������ (�� ���� � ��������).")
        voice.runAndWait()

    elif speech.find('�������') >= 0:
        voice.say("����������� ������� �������� � ���, ������������ � ������������ ��������� ���� �� ����� ������ �������� ��� ����������� �����������.")
        voice.runAndWait()

    elif speech.find('����� ����') >= 0:
        voice.say("�����������, ��� ������� ���, ����������� � �������, ���������� ����������.")
        voice.runAndWait()

    elif speech.find('������������� ����') >= 0:
        voice.say("������ ��� �������, ������������ �� ��������.")
        voice.runAndWait()

    elif speech.find('������������� ����') >= 0:
        voice.say("����, � ������� ������������� ���� ��������� �� �������� � ���� ������������� �����.")
        voice.runAndWait()

    elif speech.find('��������') >= 0:
        voice.say("�������, ������� ����� ��������� �����. ����� ��������� �������������, ?1.6�10?19 ��.")
        voice.runAndWait()

    elif speech.find('����� ���������� ������') >= 0:
        voice.say("�������������� ����� ������������� ������� ������� ���������� ��� ����� ��������������� � ��������� �������.")
        voice.runAndWait()

    elif speech.find('����������') >= 0:
        voice.say("����, ����� ������� ������������� ������ ����� ���������� �� ����������� ���� � �������������. � ����������� ���� ��������� ������.")
        voice.runAndWait()

    elif speech.find('������������') >= 0:
        voice.say("����, ����� ������� ������������� ������ �� ����� ���������� �� ����������� ���� � �������������.")
        voice.runAndWait()

    elif speech.find('������������� ���') >= 0:
        voice.say("������������� ������������ �������� ���������� ������.")
        voice.runAndWait()

    elif speech.find('���� ����') >= 0:
        voice.say("��������� �������������� ������ q, ���������� ����� ���������� ������� ����������, �� ������� ��� ����������� t.")
        voice.runAndWait()

    elif speech.find('����������') >= 0:
        voice.say("����������, ����� ������ ��������� ������������� ���� ��� ����������� ���������� �������������� ������ �� ����� ����� � ������.")
        voice.runAndWait()

    elif speech.find('������������� �������������') >= 0:
        voice.say("���������� ��������, ��������������� �������� ���������� �������������� ����������� �������������� ���� � ������ ��������� ���������� �� ������ ���������� � ���� ����, ������������ �� ����.")
        voice.runAndWait()

    elif speech.find('����� ���') >= 0:
        voice.say("���� ���� � ������� ���� ����� ��������������� ���������� �� ��� ������ � ������� ��������������� ��� �������������.")
        voice.runAndWait()

    elif speech.find('�������� �������������') >= 0:
        voice.say("���������� ��������, ������������ ������������� ���������� �� ������� �������� ������ 1 � � �������� ����������� ������� 1 �2.")
        voice.runAndWait()

    elif speech.find('�������� ���������') >= 0:
        voice.say("���������� ������ ������� ���� �����������, ������������� �������� ����� ���� �� ��������� � �������������� ������� ����.")
        voice.runAndWait()







    elif speech.find('����') >= 0 or speech.find('���'):
        voice.say('����!')
        voice.runAndWait()
        break

    else:
        voice.say('��� ������� �� ������ ����� ����� ��������')
        voice.runAndWait()
        break


    """def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', '������')
        server.sendmail('youremail@gmail.com', '����', '����������')
        server.close()


    elif speech.find('�����') >= 0 or speech.find('email') >= 0:
        try:
            voice.say("What should I say?")
            content = r()
            to = "receiver's email id"
            sendEmail(to, content)
            voice.say("Email has been sent!")
        except Exception as e:
            print(e)
            voice.say("Sorry sir. I am not able to send this email")
        voice.say("��� ������� � ��� �������� � �������, �� ��� �������������")
        voice.runAndWait()"""