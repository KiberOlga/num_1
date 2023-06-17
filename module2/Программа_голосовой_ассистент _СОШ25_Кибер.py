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
voice.say('������, ���� ����� �����, � ���� ��������� ���������.')
print('������, ���� ����� �����, � ���� ��������� ���������.')
voice.runAndWait()

while True:
    with sr.Microphone() as source:
        print('������...')
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
        voice.say(gr + "��� ���� �������")
        voice.runAndWait()

    elif speech.find('��� �� ������') >= 0 or speech.find('��� ������ ������') >= 0 or speech.find('��� �� ������') >= 0:
        voice.say("� ���� ������ ������������� � ����� ��� �� ������")
        voice.runAndWait()

    elif speech.find('youtube') >= 0 or speech.find('����') >= 0:
        webbrowser.open_new('https://www.youtube.com/')
        voice.say('� ������ ����')
        voice.runAndWait()

    elif speech.find('�����') >= 0:
        films = ["�������", "��������� ��������", "���������", "�����������", "���� - ��������"]
        gr = random.choice(films)
        voice.say("� ���� ������� ���������� ����� " + gr + ". �� ����� ���������� � ��������������.")
        voice.runAndWait()

    elif speech.find('��� ��') >= 0:
        webbrowser.open_new('https://uchi.ru/')
        voice.say('� ������ ��� ��')
        voice.runAndWait()

    elif speech.find('����') >= 0 or speech.find('�����') >= 0 or speech.find('�����') >= 0:
        webbrowser.open_new('https://mail.ru/')
        voice.say('� ������ ����� mail')
        voice.runAndWait()

    elif speech.find('���� ���') >= 0 or speech.find('���� ���') >= 0:
        webbrowser.open_new('https://phys-oge.sdamgia.ru/')
        voice.say('� ������ ���� ���� ���')
        voice.runAndWait()

    elif speech.find('����') >= 0 or speech.find('fipi') >= 0:
        webbrowser.open_new('https://fipi.ru/oge/otkrytyy-bank-zadaniy-oge#!/tab/173942232-3')
        voice.say('� ������ ���� ����')
        voice.runAndWait()

    elif speech.find('�������') >= 0 or speech.find('������') >= 0 or speech.find('�������') >= 0:
        compliment = ["� ��� �������, �����������", "�����������, ���� ��� ������", "������� ����� ���� � �������� ���������", "������� �� �������, �����������"]
        c = random.choice(compliment)
        voice.say(c)
        voice.runAndWait()

    elif speech.find('�����') >= 0 or speech.find('���� ����') >= 0 or speech.find('ok google') >= 0:
        voice.say("����� ������, ������������")
        voice.runAndWait()

    elif speech.find('������� ���� ���') >= 0 or speech.find('�������') >= 0:
        voice.say("� ���� ������� ���� ��������, ��� ����������� 7 ���, ��� ��� � ��� �������")
        voice.runAndWait()

    elif speech.find('��� ���� �����') >= 0 or speech.find('��� ��� ���') >= 0:
        voice.say("���� �� ��� �������������, � ������� ��� ���, ���� ����� �����")
        voice.runAndWait()

    elif speech.find('�����') >= 0 or speech.find("����� ������ ���") >= 0 or speech.find("�������") >= 0:
        today = datetime.now()
        today = today.strftime("%H:%M:%S")
        voice.say(f"�� ������ ������ {today}")
        voice.runAndWait()

    elif speech.find('�����') >= 0:
        speech = speech.replace("�����", "")
        url = "https://www.youtube.com/results?search_query=" + speech
        webbrowser.get().open(url)
        voice.say("� ������ " + speech + "�� youtube")
        voice.runAndWait()

    elif speech.find('google') >= 0 or speech.find('����') >= 0:
        speech = speech.replace("google", "")
        url = "https://www.google.com/search?q=" + speech
        webbrowser.get().open(url)
        voice.say("� ������ " + speech + "� Google")
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

    elif speech.find('����� ���') >= 0 or speech.find('����� ���') >= 0:
        voice.say("���� ���� � ������� ���� ����� ��������������� ���������� �� ��� ������ � ������� ��������������� ��� �������������.")
        voice.runAndWait()

    elif speech.find('�������� �������������') >= 0:
        voice.say("���������� ��������, ������������ ������������� ���������� �� ������� �������� ������ 1 � � �������� ����������� ������� 1 �2.")
        voice.runAndWait()

    elif speech.find('�������� ���������') >= 0:
        voice.say("���������� ������ ������� ���� �����������, ������������� �������� ����� ���� �� ��������� � �������������� ������� ����.")
        voice.runAndWait()



    elif speech.find('����') >= 0 or speech.find('���') >= 0:
        voice.say('����! �� ������ �������!')
        voice.runAndWait()
        break

    elif speech.find('') >= 0:
        speech = speech.replace("google", "")
        url = "https://www.google.com/search?q=" + speech
        webbrowser.get().open(url)
        voice.say("����� � ��� ���� �� ����, �� ������� " + speech + "� Google")
        voice.runAndWait()
        break
