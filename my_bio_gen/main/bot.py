import smtplib
import os
from django.shortcuts import redirect


def bot(input):

    name = input.get('username')
    phone = input.get('tel')
    email = input.get('email')
    mes = input.get('text')

    message = f'Новая заявка \n Имя: {name}\n Email: {email}\n Телефон: {phone}\n Сообщение: {mes}'

    sender = 'mybiogenbot@gmail.com'
    password = os.getenv('EMAIL_PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, 'alekss.shp@yandex.ru', f'Subject: Новая заявка {message}')
        return redirect('http://51.250.82.213/#sent')
    except Exception as _ex:
        return redirect('http://127.0.0.1:8000/#not_sent')
