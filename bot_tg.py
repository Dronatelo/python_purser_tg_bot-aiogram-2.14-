from aiogram import executor
from create_bot import dp
from handlers import start_connect,car_page_link,youtube_page_link,calculate_func,number_text,tg_link, whats_app_link, menu_handler

async def on_startup(_):
    print("Bot Online!")
    
start_connect.register_handlers_start_connect(dp)
car_page_link.register_handlers_car_link(dp)
youtube_page_link.register_handlers_youtube_link(dp)
calculate_func.register_handlers_calculate_price(dp)
number_text.register_handlers_number_linkk(dp)
tg_link.register_handlers_tg_linkk(dp)
whats_app_link.register_handlers_whtas_app_linkk(dp)
menu_handler.register_handlers_menu(dp)
    
def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    
if __name__ == '__main__':
    main()