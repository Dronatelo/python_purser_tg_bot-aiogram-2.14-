from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.main_kb import wts_tg_st

#@dp.message_handler(Text(equals = 'Номер'))
async def get_number(message: types.Message):
    await message.answer("+7************",disable_web_page_preview=True, reply_markup=wts_tg_st)
    return
    
def register_handlers_number_linkk(dp: Dispatcher):
    dp.register_message_handler(get_number, Text(equals="Номер"),state=None)
