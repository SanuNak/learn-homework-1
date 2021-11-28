"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

import setting

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': setting.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': setting.PROXY_USERNAME,
        'password': setting.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text) # ответ бота


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text) # ответ бота

def ephem_answer(update, context):

    user_text = update.message.text
    update.message.reply_text("Определяем расположение планеты")

    if len(user_text.split(" ")) == 1:
        update.message.reply_text("Ничего не введено, введите имя планеты")

    elif len(update.message.text.split(" ")) > 1:
            user_planet = user_text.split()[1].lower().strip(" ").capitalize()
            ephem_answer = getattr(ephem, user_planet, "Эту планету еще не придумали")
            if isinstance(ephem_answer, type):
                ephem_answer = ephem_answer('2021/10/1')
                constellation = ephem.constellation(ephem_answer)
                update.message.reply_text(constellation) # ответ бота
            else:
                update.message.reply_text(ephem_answer)


def main():
    # коммуникация с сервером Telegram
    mybot = Updater(setting.API_KEY, request_kwargs=PROXY, use_context=True)


    dp = mybot.dispatcher # запускаем диспитчер, он определяет тип сообщения
    dp.add_handler(CommandHandler("start", greet_user))  # если такая комманда есть, то обработч выполнит нашу функцию
    dp.add_handler(CommandHandler("planet", ephem_answer))  # если такая комманда есть, то обработч выполнит нашу функцию
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


if __name__ == "__main__":
    main()
