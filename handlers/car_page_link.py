from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.main_kb import main_menu

#@dp.message_handler(Text(equals = 'Сайт'))
async def get_car_link(message: types.Message):
    await message.answer("https://www.mobile.de/ru",disable_web_page_preview=True, reply_markup=main_menu)

    
def register_handlers_car_link(dp: Dispatcher):
    dp.register_message_handler(get_car_link, Text(equals="Сайт"),state=None)
