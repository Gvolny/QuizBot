import telebot

import datetime

import random

from auth_data import token

from upload import dwords, dwords_reverse, dwords_eng_ru, dwords_eng_ru_reverse, dwords_de_eng, dwords_de_eng_reverse

from images import get_image


def randomy(mode='DE to RU'):
    if mode == 'DE to RU' or mode is None:
        dd = dwords

    if mode == 'RU to DE':
        dd = dwords_reverse

    if mode == 'ENG to RU':
        dd = dwords_eng_ru

    if mode == 'RU to ENG':
        dd = dwords_eng_ru_reverse

    if mode == 'DE to ENG':
        dd = dwords_de_eng

    if mode == 'ENG to DE':
        dd = dwords_de_eng_reverse

    word = random.choice(list(dd.keys()))  # choose a word for translation
    get_image(word)
    print(word)
    l = list(dd.values())
    if dd[word] in l:
        (l.remove(dd[word]))
    options = list(random.sample(population=(l), k=2))  # two wrong options

    correct_option_ind = random.randint(0, 2)  # make a random index of right word

    correct_translation = dd[word]  # search right word

    options.insert(correct_option_ind, correct_translation)  # insert right word

    print(options)

    crypto = []
    crypto.append(word)
    crypto.append(correct_option_ind)
    crypto.append(options)

    print(crypto)
    print()
    print()

    return crypto


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):

        print(
            datetime.datetime.utcnow(),
            message.text,
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
        )

        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("DE to RU")
        btn2 = telebot.types.KeyboardButton("RU to DE")
        btn3 = telebot.types.KeyboardButton("ENG to RU")
        btn4 = telebot.types.KeyboardButton("RU to ENG")
        btn5 = telebot.types.KeyboardButton("DE to ENG")
        btn6 = telebot.types.KeyboardButton("ENG to DE")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, "Hello! to start the game, select the game mode.", reply_markup=markup)

    def sent_poll(message, mode):
        bot.send_message(message.chat.id, "Let's go!")


        crypi = randomy(mode=mode)

        #image = open('texted_back.png', 'rb')
        #bot.send_photo(chat_id=message.chat.id, photo=image, caption='@FrageUndAntwortSpielBot')

        animation = open('image2.gif', 'rb')
        bot.send_animation(chat_id=message.chat.id,
                           animation=animation,
                           caption='@FrageUndAntwortSpielBot'
                           )

        bot.send_poll(chat_id=message.chat.id,
                      question='Choose the correct translation of this word (' + crypi[0] + ').',
                      options=crypi[2],
                      is_anonymous=True,
                      type='quiz',
                      correct_option_id=crypi[1],
                      open_period=60
                      )


    @bot.message_handler(content_types=["text"])
    def handle_text(message):



        print(
            datetime.datetime.utcnow(),
            message.text,
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            sep='\n'
        )


        if message.text == 'DE to RU':
            mode = 'DE to RU'
            sent_poll(message, mode)

        if message.text == 'RU to DE':
            mode = 'RU to DE'
            sent_poll(message, mode)

        if message.text == 'ENG to RU':
            mode = 'ENG to RU'
            sent_poll(message, mode)

        if message.text == 'RU to ENG':
            mode = 'RU to ENG'
            sent_poll(message, mode)

        if message.text == 'DE to ENG':
            mode = 'DE to ENG'
            sent_poll(message, mode)

        if message.text == 'ENG to DE':
            mode = 'ENG to DE'
            sent_poll(message, mode)

    bot.infinity_polling(timeout=10, long_polling_timeout=5)


if __name__ == "__main__":
    telegram_bot(token)
