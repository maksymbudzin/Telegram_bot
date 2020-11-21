from datetime import datetime
from subprocess import Popen
from telegram import Bot
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from telegrambot.config import TG_TOKEN

#CALLBACK_LEFT = "call_back_left"
#CALLbACK_RIGHT = "call_back_right"
#CALLBACK_FOOTER = "call_back_footer"

#TITLES = {
  #  CALLBACK_LEFT: "нове повыдомлення",
   # CALLBACK_FOOTER: "Ще",
#}


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Перший бот Макса \n"
             "Тут є доступні команди /help та /time \n"
             "Також я можу відповісти на любе твоє пов",

    )


def do_time1(bot: Bot, update: Update):
    """ Для того щоб дізнатись час на вінді
    """
    now = datetime.now()
    text = "{}.{}.{} {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second)
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Дата та година на вінді: \n{}".format(text),
    )


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Привіт, це перший бот Макса \n"
             "Тут є доступні команди /help та /time \n"
             "Також я можу відповісти на любе твоє повідомлення",

    )


def do_echo(bot: Bot, update: Update):
    text = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
       # reply_markup=get_base_inline_keyboard()

    )


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
    )

    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    time1_handler = CommandHandler("time", do_time1)

    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time1_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()

#def get_base_inline_keyboard():
    #keyboard =[
      #     InlineKeyboardButton(TITLES[CALLBACK_LEFT]), callbackdata=CALLBACK_LEFT,
        # ],
       # [
            #InlineKeyboardButton(TITLES[CALLBACK_FOOTER]), callbackdata = CALLBACK_FOOTER,
        #],
   # ]
   # return InlineKeyboardButton(KeyError)



if __name__ == '__main__':
    main()