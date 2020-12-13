import logging
import sys

import crypto
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

sys.modules['Crypto'] = crypto

token = "1368765534:AAG7TWNlD4j83_LAJgOKoVHy2v7a-qNsugw"

import pyrebase

config = {

    "apiKey": "AIzaSyBxKG47FDkkL6rUvrQtDRfn-RGh9XbryYA",

    "authDomain": "pythonfirebasestorage-9eab0.firebaseapp.com",

    "databaseURL": "gs://pythonfirebasestorage-9eab0.appspot.com",

    "projectId": "pythonfirebasestorage-9eab0",

    "storageBucket": "pythonfirebasestorage-9eab0.appspot.com",

    "serviceAccount": "ServiceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

path_on_cloud = "Denys(48).csv"

storage.child(path_on_cloud).download(filename="Denys(48).csv", path="Denys(48).csv")

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def echo_all(message: types.Message):
    await message.reply(message.text)
    with open("C:/Users/admin/PycharmProjects/FirebaseFile/Denys(48).csv", "rb") as file:
        f = file.read()

    await bot.send_document(message.chat.id, open(r'C:/Users/admin/PycharmProjects/FirebaseFile/Denys(48).csv', 'rb'))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
# @bot.message_handler(content_types=['document'])

# def handle_docs_file(message):
#
#
#    try:
#        chat_id = message.chat.id
#
#        file_info = bot.get_file(message.document.file_id)

#        downloaded_file = bot.download_file(file_info.file_path)
#
#        src = 'C:/Users/admin/PycharmProjects/FirebaseFile/share_files/Denys(47).csv' + message.document.file_name;

#        with open(src, 'wb') as new_file:

#            new_file.write(downloaded_file)
#
#        bot.reply_to(message, "file saved")

#    except Exception as e:

#        bot.reply_to(message, e)
#
# bot.polling()
