from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings.file_settings import API_KEY_TG

bot = Bot(token=API_KEY_TG)
dp = Dispatcher(bot, storage=MemoryStorage())
        