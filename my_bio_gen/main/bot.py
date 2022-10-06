from email import message
import smtplib
import os

from email.mime.text import MIMEText

def bot(input):

    name = input.get('username')
    phone = input.get('tel')
    email = input.get('email')
    mes = input.get('text')

    message = f'Новая заявка \n Имя: {name}\n Email: {email}\n Телефон: {phone}\n Сообщение: {mes}'
    msg = MIMEText(message)
    msg['Subject'] = 'Новая заявка'
    sender = 'mybiogenbot@gmail.com'
    password = os.getenv('EMAIL_PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, password)
    server.sendmail(sender, 'alekss.shp@yandex.ru', msg.as_string())
