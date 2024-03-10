from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.main_kb import nb_tg_st

#@dp.message_handler(Text(equals = 'WhatsApp'))
async def get_whats_app_link(message: types.Message):
    await message.answer("https://wa.me/message/***********",disable_web_page_preview=True, reply_markup=nb_tg_st)
    return
    
def register_handlers_whtas_app_linkk(dp: Dispatcher):
    dp.register_message_handler(get_whats_app_link, Text(equals="WhatsApp"),state=None)
