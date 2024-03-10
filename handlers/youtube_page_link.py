from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.main_kb import main_menu

#@dp.message_handler(Text(equals = 'YouTube'))
async def get_youtube_link(message: types.Message):
    await message.answer("https://www.youtube.com/********",reply_markup=main_menu)
    return
    
def register_handlers_youtube_link(dp: Dispatcher):
    dp.register_message_handler(get_youtube_link, Text(equals="YouTube"),state=None)
