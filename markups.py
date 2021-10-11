from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, inline_keyboard
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData

btnMain = KeyboardButton('Bosh menyu')

btnUz = KeyboardButton("Uz")
btnRu = KeyboardButton("Ru")
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnUz, btnRu)

by_callback = CallbackData("avt")
keyboard = InlineKeyboardMarkup(row_width=2)
avt_button = InlineKeyboardButton(text="Avtorizatsiya", callback_data=by_callback.new())
reg_button = InlineKeyboardButton("Registratsiya", url='https://hostmaster.uz/site/signup/' ,callback_data='/start')
keyboard.insert(avt_button)
keyboard.insert(reg_button)

btnKontakt = KeyboardButton("Mening Kontaktlarim")
btnService = KeyboardButton("Mening xizmatlarim")
btnSetting = KeyboardButton("Sozlamalar")
btnReg1 = KeyboardButton("Reg/avtorizatsiya")
btnPayment = KeyboardButton("To'lov")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnKontakt).add(btnService).add(btnPayment).add(btnReg1).add(btnSetting)

btnVDS = KeyboardButton("Mening VDS larim")
btnDomen = KeyboardButton("Menig Domenlarim")
btnXost = KeyboardButton("Mening Xostlarim")
btnServer = KeyboardButton("Mening serverlarim")
serviceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnVDS).add(btnDomen).add(btnXost).add(btnServer)

