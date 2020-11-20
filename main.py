import telebot
from telebot import types
import db_users


bot = telebot.TeleBot("1299818980:AAFzO8-7l_0iKWoe2hgQopIg0Aw28BJouNM")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ОТЗЫВЫ")
    item2 = types.KeyboardButton("ГАРАНТИИ")
    item3 = types.KeyboardButton("VIP ЧАТ")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}! </b>\nЧто желаешь?",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text
    db_users.check_and_add_user(message)

    if get_message_bot == "VIP ЧАТ":
        bot.send_message(message.chat.id, "Стоимость VIP и как оплатить? "
                                          "\n\n— Стоимость VIP составляет 300 рублей"
                                          "\n\n— Оплата производится на карту 4890XXXX3095503 "
                                          "\n\n— Оплата через мобильное приложение Cбербанка \nПлатежи ️ Другому Человеку  В другой банк  По номеру карты."
                                          "\n\n— Оплата через мобильное приложение Альфа Банк \nПлатежи ️ В другой банк ️ По номеру карты "
                                          "\n\n— Оплата через QIWI  \nПереводы ️  Перевод на карту \n\nПосле оплаты предоставьте чек операции нашему Администратору в ЛС, после чего он выдаст вам ссылку в закрытый канал - @kostii "
                                          "\n\nС другими Банками и электронными кошельками абсолютно аналогично!",
                         parse_mode='html', )

    if get_message_bot == "ОТЗЫВЫ":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Отзывы", url="https://t.me/sochineniye_otzyv"))
        bot.send_message(message.chat.id, "Переходи в наш канал с отзывами ", parse_mode='html', reply_markup=markup)

    if get_message_bot == "ГАРАНТИИ":
        bot.send_message(message.chat.id,"Самый популярный вопрос, - Почему я должен верить вам, где гарантии?\n\nГарантии это наши отзывы с 2019 года, которые вы можете посмотреть в нашем канале с отзывами, а ещё то, что мы выкладываем на своём канале. А публикуем мы, помимо просто ответов, также фото реальных КИМов ЕГЭ. Все задания в них уникальны и вы можете это проверить сами. И вот скажите, где вы ещё кроме нас такое видели? Максимум, что вы могли видеть, так это фото распечатанных КИМов с заданиями прошлогодней давности, которые легко пробиваются или гуглятся в интернете.",parse_mode='html')


bot.polling()