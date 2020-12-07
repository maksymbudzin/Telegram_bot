import sys
import crypto
import telebot

sys.modules['Crypto'] = crypto

token = "1235237928:AAHx2eMyr8aMi2CJSW5h9gubXbA5ObJ-vnI"

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

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def echo_all(message):

    with open("C:/Users/admin/PycharmProjects/FirebaseFile/Denys(48).csv", "rb") as file:
        f = file.read()

    bot.reply_to(message, "Завантажую файл")

    bot.send_document(message.chat.id, open(r'C:/Users/admin/PycharmProjects/FirebaseFile/Denys(48).csv', 'rb'))

    bot.reply_to(message, "Файл отримано")


bot.polling()

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
