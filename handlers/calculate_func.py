from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.main_kb import main_menu,call_menu,menu
from create_bot import bot
from settings.requests_func import get_all_params,price_calculate

class get_calculate_price(StatesGroup):
    get_calculate=State()

#@dp.message_handler(Text(equals = 'Расчёт'))
async def get_auto_link(message: types.Message):
    await message.answer("Вставьте ссылку на интересующий Вас автомобиль!", reply_markup=menu)
    await get_calculate_price.get_calculate.set()

#@dp.message_handler(state="*",commands = "cancel")
#@dp.message_handler(Text(equals='cancel',ignore_case=True),state="*")
async def cancel_handler(message: types.Message,state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Вы возвращены в меню!",reply_markup=main_menu)

#@dp.message_handler(state=get_weather_info.wather_info)
async def get_calculate_info(message: types.Message, state: FSMContext):
    auto_link = message.text
    
    
    if auto_link == "Меню" or auto_link == "/start":
        await message.answer('Вы возвращены в меню.', reply_markup=main_menu)
        await state.finish()
        return
    
    if not auto_link.startswith("https://www.mobile.de/"):
        await message.answer('Некорректная ссылка или введёная информация. \nПомните, что ссылка для расчёта должна начинаться с "https://www.mobile.de/".',disable_web_page_preview=True, reply_markup=main_menu)
        await state.finish()
        return
 
    else:
        await message.answer('Подождите, идет расчет, расчет может занять 1-3 минуты, в редких случаях до 30 минут.', reply_markup=menu)
        params_result = get_all_params(auto_link)
        a, b, c, d = params_result
        res1,res2,res3 = price_calculate(a,b,c,d)
        channel_id = -1
        sms_text = (f'https://t.me/{message.from_user.username}' +'\n\n'+ f'{auto_link}')

        full_text = (
            "Что включено в стоимость: \n\n"

            "<b>- Запрос к дилеру в Германии (запрос технического состояния, аварийность, оригинальность пробега, сервисная история, юридическая чистота)\n </b>"
            "<b>- Оплата автомобиля, оформление экспортных документов и номеров\n </b>"
            "<b>- Услуги по доставки автомобиля своим ходом\n </b>"
            "<b>- Таможенные платежи\n </b>"
            "<b>- Возврат немецкого НДС (вы сразу покупаете машину по цене Нетто)\n </b>" 
            "<b>- Оформление СБКТС, ЭПТС и оплату утилизационного сбора от вашего лица.\n </b>"
            "<b>- Возможна постановка на учет в ГИБДД\n\n </b>"

            "Оплата:\n\n"

            "<b>Для заключения договора поставки автомобиля, нужно: </b>\n"
            "<b> - определиться с автомобилем </b>\n"
            "<b> - проверить автомобиль </b>\n"
            "<b> - договориться с дилером и заключить контракт с дилером на выкуп конкретного автомобиля. </b>\n\n"

            "<i> Только после того, как мы бесплатно подберем автомобиль, мы заключаем с вами договор поставки конкретного автомобиля, и вы вносите аванс 30%\n </i>"
            "<i> Окончательный расчёт происходит после доставки автомобиля в Москву.\n\n </i>"
            "<b> Сроки доставки 2-4 недели\n\n </b>"

            "Номер – связаться по Телефону\n"
            "WhatsApp – связаться по WhatsApp\n"
            "Telegram – связаться в Telegram"
        )
        
        if isinstance(res1, float) and isinstance(res3, str):

            await message.answer(f"<b> {res2} </b>" + "\n\n" +
                                 "==============================\n"+
                         '?? Окончательная стоимость "<b>ПОД КЛЮЧ</b>" в Москве: €' + f"{res1}\n" +
                         "=============================="+"\n\n" +
                         '??<b>ВНИМАНИЕ</b>, на любой автомобиль можно купить <b>ГАРАНТИЮ</b>??\n\n'+
                         f"{auto_link}" + "\n\n"+
                         full_text,parse_mode=types.ParseMode.HTML, disable_web_page_preview=True, reply_markup=call_menu)
            
            await state.finish()
            await bot.send_message(chat_id=channel_id, text=sms_text)
            return

        if isinstance(res1, float) and isinstance(res3, int):     
                                 
            await message.answer(f"<b> {res2} </b>" + "\n\n" +
                                 "==============================\n"+
                         '?? Окончательная стоимость "<b>ПОД КЛЮЧ</b>" в Москве: €' + f"{res1}\n" +
                         "=============================="+"\n\n" +
                         '??<b>ВНИМАНИЕ</b>, на любой автомобиль можно купить <b>ГАРАНТИЮ</b>??\n\n'+
                         f"{auto_link}" + "\n\n"+
                         full_text,parse_mode=types.ParseMode.HTML,disable_web_page_preview=True, reply_markup=call_menu)
            await state.finish()
            await bot.send_message(chat_id=channel_id, text=sms_text)
            return

        if isinstance(res3, int) and res3 < 0: 
            await message.answer(f"<b> {res1} </b>" + "\n\n" + f'<b> {res2} </b>',parse_mode=types.ParseMode.HTML, disable_web_page_preview=True, reply_markup=main_menu)
            await state.finish()
            return
        
        if a == "0" and b == 0 and c == "09/2020" and d == 0: 
            await message.answer("Сервера перегружены! Пожалуйста, обратитесь к нашему менеджеру или попробуйте ещё раз.", reply_markup=call_menu)
            await state.finish()
            return
            
        else: 
            await message.answer("Ошибка расчёта! Пожалуйста, обратитесь к нашему менеджеру!", reply_markup=call_menu)
            await state.finish()
            return


def register_handlers_calculate_price(dp: Dispatcher):
    dp.register_message_handler(get_auto_link, Text(equals="Расчёт") | Text(equals="Новый расчёт"), state=None)
    dp.register_message_handler(cancel_handler,state="*",commands="cancel")
    dp.register_message_handler(cancel_handler,Text(equals='cancel',ignore_case=True),state="*")
    dp.register_message_handler(get_calculate_info,state=get_calculate_price.get_calculate)
