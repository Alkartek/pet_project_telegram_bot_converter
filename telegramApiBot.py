import telebot
from telebot import types
import actual_convert
import config

bot = telebot.TeleBot(config.TOKEN)






@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Understadebl")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, я могу сказать сколько у тебя сейчас денежек в какой валюте", reply_markup=markup)

@bot.message_handler(commands=['value'])
def value(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Understadebl")
    markup.add(btn1)
    bot.send_message(message.from_user.id, f'Нынешний курс Euro = {actual_convert.curse_eu()}, Dollars = {actual_convert.curse_us()}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться' or message.text == 'Understadebl':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Сколько у меня Рубли')
        btn2 = types.KeyboardButton('Сколько у меня Доллары')
        btn3 = types.KeyboardButton('Сколько у меня Евро')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос, какая валюта вам интересана?', reply_markup=markup) #ответ бота


    if message.text == 'Сколько у меня Рубли':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сколько у меня Доллары')
        btn2 = types.KeyboardButton('Сколько у меня Евро')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, f'У вас сейчас {actual_convert.rubls()} рублей', reply_markup=markup)

    if message.text == 'Сколько у меня Доллары':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton('Спасибо')
        markup.add(btn3)
        bot.send_message(message.from_user.id, f'у вас сейчас {actual_convert.dollars()} баксов', reply_markup=markup)

    if message.text == 'Спасибо':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Сколько у меня Рубли')
        btn2 = types.KeyboardButton('Сколько у меня Доллары')
        btn3 = types.KeyboardButton('Сколько у меня Евро')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Всего хорошего, если что, я всегда подскажу чтолько у вас денежек :)',
                         reply_markup=markup)  # ответ бота


    if message.text == 'Сколько у меня Евро':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton('Спасибо')
        markup.add(btn3)
        bot.send_message(message.from_user.id, f'У вас сейчас {actual_convert.euro()} евриков', reply_markup=markup)



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть