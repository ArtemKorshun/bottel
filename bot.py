import telebot
from telebot import types
bot = telebot.TeleBot('1035129916:AAHpPba3GKcaWhYrwtEsVw6TJlXQ0XUALvI')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('хочу учавствовать', 'вопрос')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'хочу учавствовать':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'вопрос':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://телеграм.онлайн/#/im?p=@korshun_pro")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'Прощай, создатель', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def run_message(message):
    keyboard2 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://телеграм.онлайн/#/im?p=@korshun_pro")
    keyboard2.add(url_button)
    bot.send_message(message.chat.id, 'Пиши сюда', reply_markup=keyboard2)
bot.polling()

