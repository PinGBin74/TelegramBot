import telebot
from telebot import types

token = "7100264702:AAEoua5LID79xwVjjjmLemnHGsYl4fGagzI"
bot = telebot.TeleBot(token)

student_info = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton("Программирование", callback_data="programming")
    but2 = types.InlineKeyboardButton("Физическая культура", callback_data="physical")
    but3 = types.InlineKeyboardButton("Основы профессиональной деятельности", callback_data="professional")
    but4 = types.InlineKeyboardButton("Математика", callback_data="mathematics")
    markup.add(but1, but2, but3, but4)
    bot.send_message(message.chat.id, "Выберите дисциплину:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global student_info

    if call.data in ["programming", "physical", "professional", "mathematics"]:
        markup = types.InlineKeyboardMarkup(row_width=2)
        but1 = types.InlineKeyboardButton("Иван Иванов", callback_data="1")
        but2 = types.InlineKeyboardButton("Дима Билан", callback_data="2")
        but3 = types.InlineKeyboardButton("Артур Пирожков", callback_data="3")
        but4 = types.InlineKeyboardButton("Пупкин Иван", callback_data="4")
        markup.add(but1, but2, but3, but4)
        bot.send_message(call.message.chat.id, "Выберите студента:", reply_markup=markup)

    elif call.data in ["1", "2", "3", "4"]:
        student_names = {
            "1": {"name": "Иван Иванов", "attendance": "90%", "marks": "5"},
            "2": {"name": "Дима Билан", "attendance": "80%", "marks": "4"},
            "3": {"name": "Артур Пирожков", "attendance": "70%", "marks": "3"},
            "4": {"name": "Пупкин Иван", "attendance": "60%", "marks": "2"}
        }
        student_info = student_names.get(call.data, {})

        markup = types.InlineKeyboardMarkup(row_width=2)
        but1 = types.InlineKeyboardButton("Посещаемость", callback_data="attendance")
        but2 = types.InlineKeyboardButton("Оценки", callback_data="marks")
        markup.add(but1, but2)
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Информация о студенте: {student_info.get('name')}",
                         reply_markup=markup)

    elif call.data == "attendance":
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Посещаемость: {student_info.get('attendance')}")

    elif call.data == "marks":
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Оценки: {student_info.get('marks')}")

if __name__ == '__main__':
    bot.polling(none_stop=True)
