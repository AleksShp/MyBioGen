import telegram

from telegram import Bot, message


def bot(input):
    bot = Bot(token='5485824035:AAHu2wvsspm8kwscgWpHe5DkWnMLDdD3Ms0')

    chat_id = 969030499

    name = input.get('username')
    phone = input.get('tel')
    email = input.get('email')
    mes = input.get('text')

    message = f'Новая заявка \n Имя: {name}\n Email: {email}\n Телефон: {phone}\n Сообщение: {mes}'

    text = message

    bot.send_message(chat_id, text)
