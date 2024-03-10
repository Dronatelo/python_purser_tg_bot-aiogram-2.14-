from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.main_kb import main_menu

#@dp.message_handler(Text(equals = 'Меню'))
async def get_menu(message: types.Message):
    await message.answer("Вы возвращены в меню.",disable_web_page_preview=True, reply_markup=main_menu)

    
def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(get_menu, Text(equals="Меню"),state=None)
