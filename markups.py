from typing import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, inline_keyboard
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData

btnCancel = KeyboardButton("Bosh sahifaga qaytish")
btnCancelru = KeyboardButton("Bернуться в главное меню")

btnUz = KeyboardButton("🇺🇿Uz")
btnRu = KeyboardButton("🇷🇺Ru")
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnUz).add(btnRu)

"uz inline keyboard"
by_callback = CallbackData("Avt")
keyboard = InlineKeyboardMarkup(row_width=2)
avt_button = InlineKeyboardButton(text="Avtorizatsiya", callback_data=by_callback.new())
reg_button = InlineKeyboardButton(text="Registratsiya", url='https://hostmaster.uz/site/signup/\nuz' ,callback_data='/start')
keyboard.insert(avt_button)
keyboard.insert(reg_button)

"ru inline keyboard"
by_callback = CallbackData("Avt ru")
keyboardru = InlineKeyboardMarkup(row_width=2)
avtru_button = InlineKeyboardButton(text="Авторизация", callback_data=by_callback.new())
regru_button = InlineKeyboardButton(text="Регистрация", url='https://hostmaster.uz/site/signup/\nru' ,callback_data='/start1')
keyboardru.insert(avtru_button)
keyboardru.insert(regru_button)

"uz MainMenu"
btnKontakt = KeyboardButton("Mening kontaktlarim")
btnService = KeyboardButton("Mening xizmatlarim")
btnSetting = KeyboardButton("Sozlamalar")
btnReg1 = KeyboardButton("Reg/avtorizatsiya")
btnPayment = KeyboardButton("To'lov")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnKontakt).add(btnService).add(btnPayment).add(btnReg1).add(btnSetting)

"uz service"
btnVDS = KeyboardButton("Mening VDS larim")
btnDomen = KeyboardButton("Menig Domenlarim")
btnXost = KeyboardButton("Mening Xostlarim")
btnServer = KeyboardButton("Mening Serverlarim")
serviceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnVDS).add(btnDomen).add(btnXost).add(btnServer).add(btnCancel)

"ru MainMenu"
btnKontaktru = KeyboardButton("Мои контакты")
btnServiceru = KeyboardButton("Мои услуги")
btnSettingru = KeyboardButton("Настройки")
btnReg1ru = KeyboardButton("Рег/авторизация")
btnPaymentru = KeyboardButton("Оплата")
otherMenuru = ReplyKeyboardMarkup(resize_keyboard=True).add(btnKontaktru).add(btnServiceru).add(btnPaymentru).add(btnReg1ru).add(btnSettingru)

btnVDSru = KeyboardButton("Мои VDS")
btnDomenru = KeyboardButton("Мои Домены")
btnXostru = KeyboardButton("Мои Хостинги")
btnServerru = KeyboardButton("Мои Сервера")
serviceruMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnVDSru).add(btnDomenru).add(btnXostru).add(btnServerru).add(btnCancelru)

"uz Setting"
btnSetUz = KeyboardButton("🇺🇿uz")
btnSetRu = KeyboardButton("🇷🇺ru")
setlangMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSetUz).add(btnSetRu)
