from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

web_page = KeyboardButton("Сайт")
calculate_func = KeyboardButton("Расчёт")
youtube_channel = KeyboardButton("YouTube")
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(web_page, calculate_func, youtube_channel)

start_button = KeyboardButton("/start")
start_bt = ReplyKeyboardMarkup(resize_keyboard=True)
start_bt.add(start_button)

menu_bt = KeyboardButton("Меню")
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(menu_bt)

number = "Номер"
whtas_link = "WhatsApp"
tg_link = "Telegram"
new_calculate = "Новый расчёт"

call_menu = ReplyKeyboardMarkup(resize_keyboard=True)
call_menu.add(number, whtas_link, tg_link,new_calculate,menu_bt)



wts_tg_st = ReplyKeyboardMarkup(resize_keyboard=True)
wts_tg_st.add(whtas_link, tg_link, start_button)

nb_tg_st = ReplyKeyboardMarkup(resize_keyboard=True)
nb_tg_st.add(number, tg_link, start_button)

nb_wts_st = ReplyKeyboardMarkup(resize_keyboard=True)
nb_wts_st.add(number, whtas_link, start_button)
