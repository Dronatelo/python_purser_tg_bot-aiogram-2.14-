from aiogram import types,Dispatcher
from keyboards.main_kb import main_menu

#@dp.message_handler(commands='start',state=None)
async def start(message: types.Message, state=None):

    text = "*Расчет стоимости автомобиля из Германии под заказ. *"\
           "*Для этого мне нужна ссылка с русской версии сайта mobile.de/ru. *\n\n"\
           "— Машины старше 5 лет высокая таможенная пошлина и их ввозить не выгодно.\n"\
           "— На машины до трех лет высокая стоимость таможни (48% от стоимости), поэтому не удивляйтесь цене, но мы придумаем как снизить итоговую стоимость.\n"\
           "— Доставка под ключ в среднем 2-4 недели.\n\n"\
           "— Оплата по факту прихода автомобиля, но авансовый платеж «серьёзности намерений» - 30%\n\n"\
           "— Работаем через договор, оплата в рублях по курсу ЦБ.\n\n"\
           "Сайт – Ссылка на сайт с автомобилями\n"\
           "Расчёт – Произвести расчёт стоимости автомобиля\n"\
           "YouTube – Ссылка на наш YouTube канал"\
    
    await message.answer(text,parse_mode=types.ParseMode.MARKDOWN,disable_web_page_preview=True, reply_markup=main_menu)
    
    return
def register_handlers_start_connect(dp: Dispatcher):
    dp.register_message_handler(start,commands="start",state=None)
