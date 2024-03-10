from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.main_kb import nb_tg_st

#@dp.message_handler(Text(equals = 'Telegram'))
async def get_tg_link(message: types.Message):
    await message.answer("https://t.me/*********",disable_web_page_preview=True, reply_markup=nb_tg_st)
    return
    
def register_handlers_tg_linkk(dp: Dispatcher):
    dp.register_message_handler(get_tg_link, Text(equals="Telegram"),state=None)
