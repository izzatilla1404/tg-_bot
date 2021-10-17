from typing import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, message, user
from aiogram.types.callback_query import CallbackQuery
from aiogram.types.reply_keyboard import KeyboardButton
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text
from config import API_TOKEN
import markups as nav
import logging
# import db
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# from languages import setup_middleware
# i18n = setup_middleware(dp)
# _ = i18n.gettext
# LANG_STORAGE = {}
# LANGS = ["uz", "ru"]

"start"
@dp.message_handler(commands=['start'])
async def comand_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Salom {0.first_name} tilni tanlang\nПривет {0.first_name} выберите язык".format(message.from_user), reply_markup = nav.mainMenu)

"select language"
@dp.message_handler(Text(equals=["🇺🇿Uz", "🇷🇺Ru"]))
async def bot_message(message: types.Message):
    if message.text == "🇺🇿Uz":
        await bot.send_message(message.from_user.id, "Siz o'zbek tilini tanladingiz\nAgar ro'yxatdan o'tgan bo'lsangiz 'Avtorizatsiya'ni bosing\nAgar ro'yxatdan o'tmagan bo'lsangiz 'Registratsiya'ni bosing", reply_markup=nav.keyboard)
    if message.text == "🇷🇺Ru":
        await bot.send_message(message.from_user.id, "Вы выбрали русский язык\nЕсли вы зарегистрированы, нажмите 'Авторизация'\nЕсли вы не зарегистрированы, нажмите 'Регистрация'", reply_markup=nav.keyboardru)
    
"uz inline"
@dp.callback_query_handler(Text(equals=["Avt"]))
async def calluz(call: CallbackQuery):
    await call.answer(cache_time=60)
    # callback_data = call.data
    # logging.info(f"call = {callback_data}")
    await call.message.answer("Siz 'Avtorizatsiya'ni tanladiz\nElektron pochta manzilingizni kiriting")

"ru inline"
@dp.callback_query_handler(text_contains="Avt ru")
async def callru(call: CallbackQuery):
    await call.answer(cache_time=60)
    # callback_data = call.data
    # logging.info(f"call = {callback_data}")
    await call.message.answer("Вы выбрали 'Авторизация'\nВведите свой адрес электронной почты")  

"mail and password"
@dp.message_handler(text_endswith=['.com', '.ru', '.uz'])
async def text_endswith_handler(message: types.Message):
    # if message in list:
    await bot.send_message(message.from_user.id, "Siz royxatdan otdingiz", reply_markup=nav.otherMenu)
    # else:
    #     await bot.send_message(message.from_user.id, _("emilingiz bazada yoq"), nav.keyboard)

# reply_markup=nav.otherMenu

"service UZ"
@dp.message_handler(Text(equals=["Mening xizmatlarim"]))
async def serviceuz(message: types.Message):
    await bot.send_message(message.from_user.id, "Siz xizmatlarni tanladingiz", reply_markup=nav.serviceMenu)

@dp.message_handler(Text(equals=["Mening Hostlarim"]))
async def hostuz(message: types.Message):
    await bot.send_message(message.from_user.id, "Siz 'host'larni tanladingiz")

@dp.message_handler(Text(equals=["Menig Domenlarim"]))
async def domenuz(message: types.Message):
    await bot.send_message(message.from_user.id, "Siz 'domen'larni tanladingiz")

@dp.message_handler(Text(equals=["Mening VDS larim"]))
async def vdsuz(message: types.Message):
    await bot.send_message(message.from_user.id, "Siz 'vds'larni tanladingiz")

@dp.message_handler(Text(equals=["Mening serverlarim"]))
async def serveruz(message: types.Message):
    await bot.send_message(message.from_user.id, "Siz 'server'larni tanladingiz")

@dp.message_handler(Text(equals=["Bosh sahifaga qaytish"]))
async def canceluz(message: types.Message):
    await bot.send_message(message.from_user.id, "Siz bosh sahiga qaytindingiz", reply_markup=nav.otherMenu)

"service RU"
@dp.message_handler(Text(equals=["Мои услуги"]))
async def serviceru(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы выбрали услуги", reply_markup=nav.serviceruMenu)

@dp.message_handler(Text(equals=["Мои Хостинги"]))
async def hostru(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы выбрали 'хосты'")

@dp.message_handler(Text(equals=["Мои Домены"]))
async def domenru(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы выбрали 'домены'")

@dp.message_handler(Text(equals=["Мои VDS"]))
async def vdsru(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы выбрали 'vds'")

@dp.message_handler(Text(equals=["Мои Сервера"]))
async def serverru(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы выбрали 'серверы'")

@dp.message_handler(Text(equals=["Bернуться в главное меню"]))
async def cancelru(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы вернулись в главное меню", reply_markup=nav.otherMenu)

"Setting change language"
@dp.message_handler(Text(equals=["Sozlamalar","Настройки"]))
async def bot_messege(message: types.Message):
    if message.text == "Sozlamalar":
        await bot.send_message(message.from_user.id, "Tilni tanlang", reply_markup=nav.setlangMenu)
    elif message.text == "Настройки":
        await bot.send_message(message.from_user.id, "Выберите язык", reply_markup=nav.setlangMenu)

@dp.message_handler(Text(equals=["🇺🇿uz", "🇷🇺ru"]))  
async def bot_message(message: types.Message):
    if message.text == "🇺🇿uz":
        await bot.send_message(message.from_user.id, "Siz O'zbek tilini tanladingiz" ,reply_markup=nav.otherMenu)
    elif message.text == "🇷🇺ru":
        await bot.send_message(message.from_user.id, "Вы выбрали русский язык" ,reply_markup=nav.otherMenuru)







# if db.execute_read_query(message.from_user.id):
#     await bot.send_message(message.from_user.id, "siz avtoregdan otmagansiz", reply_markup=nav.keyboard)
# else:
#     await bot.send_message(message.from_user.id, "siz royxatdan otgansiz", reply_markup=nav.otherMenu)

# @dp.message_handler(text_contains=(message))
# async def reg(message: types.Message):
#     if message.from_user.id in db.users:
#         await bot.send_message(message.from_user.id, "avtoregdan otdingiz")
#     else:
#         await bot.send_message(message.from_user.id, "siz bazadan topilmadizz")

# @dp.message_handler(Text(equals=["Registratsiya", "Avtorizatsiya"]))
# async def bot_message(message: types.Message):
#     if message.text == "Avtorizatsiya":
#         await bot.send_message(message.from_user.id, "gmailni yozing")
#         # await bot.send_message(message.from_user.id, "parol yozin")
#         if(not db.user_exists(message.from_user.id)):
#             # db.add_user(message.from_user.id)
#             await bot.send_message(message.from_user.id, "siz avtoregdan otmagansiz", reply_markup=nav.keyboard)
#         else:
#             await bot.send_message(message.from_user.id, "siz royxatdan otgansiz", reply_markup=nav.otherMenu)
#     elif message.text == "Registratsiya":
#         await bot.send_message(message.from_user.id, "siz regni tanladiz")
    
# @dp.message_handler()
# async def bot_message(message: types.Message):
#     if message.chat.text == 'private':
#         if message.text == 'Mening Domenlarim':
#             pass
#         else:
#             if db.get_signup(message.from_user.id) == "setnickname":
#                 if(len(message.text) > 20):
#                     await bot.send_message(message.from_user.id, "nick kop sozlar bor 20-tadan")
#                 else:
#                     db.set_nickname(message.from_user.id, message.text)
#                     db.set_signup(message.from_user.id, "done")
#                     await bot.send_message(message.from_user.id, "registratsiyadan otdingiz", reply_markup=nav.mainMenu)
#             else:
#                 await bot.send_message(message.from_user.id, "nima?")

# @dp.message_handler()
# async def bot_message(message: types.Message):
#     if message.chat.type == 'private':
#         await bot.send_message(message.from_user.id, message.text)

# @dp.callback_query_handler(text="btnLanguage")
# async def language(message:types.Message):
#     await bot.delete_message(message.from_user.id, message.message.message_id)
#     await bot.send_message(message.from_user.id, "siz tanlagan til", reply_markup=nav.mainMenu)       

# @dp.message_handler(commands=['start'])
# async def process_hello(message: types.Message):
#      await bot.send_message(message.from_user.id, 'salom', 
#    reply_markup=kb.greet_kb)
# async def process_start(message: types.Message):
#     await bot.send_message(message.from_user.id, 'salom {0.first_name}'.format(message.from_user))
# user_dict = {}

# class User:
#     def __init__(self, name):
#         self.name = name
#         keys = ['gmail' , 'password', 'return_password']
#         for key in keys:
#             self.key = None

# @dp.message_handler(commands=['start'])
# async def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     itembtn1 = types.KeyboardButton('/reg')
#     itembtn2 = types.KeyboardButton('/avtorizatsiya')
#     itembtn3 = types.KeyboardButton('/menu')
#     markup.add(itembtn1, itembtn2, itembtn3)

#     await bot.send_message(message.chat.id, "salom "
#     + message.from_user.first_name
#     + " ", reply_markup=markup)

# @dp.message_handler(commands=["reg"])
# async def process_gmail_step(message):
#     try:
#         chat_id = message.chat.id
#         user_dict[chat_id] = User(message.text)
#         msg = bot.send_message(chat_id, 'elektron pochtangizni yozing')
#         await bot.register_next_step_handler(msg, process_gmail_step)
#     except Exception as e:
#         await bot.reply_to(message, 'ooops!!')

# async def process_password_step(message):
#     try:
#         chat_id = message.chat.id
#         user = user_dict[chat_id]
#         user.fullname = message.text
#         msg = bot.send_message(chat_id, 'parol')
#         await bot.register_next_step_handler(msg, process_password_step)
#     except Exception as e:
#         await bot.reply_to(message, 'ooops!!')

# async def process_password2_step(message):
#     try:
#         chat_id = message.chat.id
#         user = user_dict[chat_id]
#         user.phone = message.text
#         msg = bot.send_message(chat_id, 'parolni qayta kiriting')
#         await bot.register_next_step_handler(msg, process_password2_step)
#     except Exception as e:
#         await bot.register_next_step_handler(msg, process_password2_step)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)